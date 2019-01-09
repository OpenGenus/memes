import os
import sys
import ctypes  # for windows
from getpass import getpass
from configparser import ConfigParser

# import for uploading images to imgur
from imgurpython import ImgurClient

# imports for authenticating using selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# imports for twitterAPI
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs
from TwitterAPI import TwitterAPI

def set_desktop_background(img_path):
    platform = sys.platform

    if platform == 'win32':
        '''
        Windows
        '''
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)

    elif platform == 'Darwin':
        '''
        Macintosh
        '''
        print('No support for Mac yet.')

    elif platform == 'linux' or platform == 'linux2':
        '''
        Linux
        '''
        sessionName = os.getenv("DESKTOP_SESSION")

        if sessionName == 'gnome':
            os.system(
                "gsettings set org.gnome.desktop.background picture-uri file:" + img_path)

        elif sessionName == 'kde':
            print('No support for KDE systems yet.')

        elif sessionName == 'xfce':
            print('No support for xfce systems yet.')

        elif sessionName == 'i3':
            os.system("feh --bg-scale " + img_path)


def upload_to_imgur(img_path):
    config = ConfigParser()
    config.read('auth.ini')

    client_id = config.get('imgur_credentials', 'client_id')
    client_secret = config.get('imgur_credentials', 'client_secret')

    client = ImgurClient(client_id, client_secret)

    user_res = input("Do you want to upload anonymously to imgur?(yes/no)")

    if user_res.lower() == 'no':
        try:
            imgur_username = input("Enter username:")
            imgur_password = getpass("Enter password:")
            firefox_driver_path = os.getcwd() + os.sep + 'drivers' + os.sep + 'geckodriver'

            authorization_url = client.get_auth_url('pin')

            driver = webdriver.Firefox(executable_path=firefox_driver_path)
            driver.get(authorization_url)

            username = driver.find_element_by_xpath('//*[@id="username"]')
            password = driver.find_element_by_xpath('//*[@id="password"]')

            username.clear()
            password.clear()

            username.send_keys(imgur_username)
            password.send_keys(imgur_password)

            driver.find_element_by_id("allow").click()

            timeout = 5

            try:
                element_present = expected_conditions.presence_of_element_located(
                    (By.ID, 'pin'))
                WebDriverWait(driver, timeout).until(element_present)
                pin_element = driver.find_element_by_id('pin')
                pin = pin_element.get_attribute("value")

            except TimeoutException as e:
                print(e)

            driver.close()
            # print(pin)
            credentials = client.authorize(pin, 'pin')
            client.set_user_auth(
                credentials['access_token'], credentials['refresh_token'])

            config = {
                    'album': None,
                    'name': 'test name',
                    'title':  'test title',
                    'description': 'test description'
            }
            print("Uploading image...")
            image = client.upload_from_path(
                img_path, config=config, anon=False)
            print("Done! Check at", image['link'])

        except Exception as e:
            print(e)

    elif user_res.lower() == 'yes':
        try:
            response = client.upload_from_path(img_path)

        except Exception as e:
            print(e)

        else:
            print('Upload Successful! Check at', response['link'])


def upload_to_twitter(img_path):

    config = ConfigParser()
    config.read('auth.ini')
    consumer_key = config.get('twitter_credentials', 'api_key')
    consumer_secret = config.get('twitter_credentials', 'api_secret')

    oauth = OAuth1(consumer_key, consumer_secret)
    res = requests.post(
        url='https://api.twitter.com/oauth/request_token', auth=oauth)

    credentials = parse_qs(res.text)
    request_key = credentials.get('oauth_token')[0]
    request_secret = credentials.get('oauth_token_secret')[0]

    authorization_url = 'https://api.twitter.com/oauth/authorize?oauth_token=%s' % request_key

    print('Go to the following URL to fetch the verifier token:', authorization_url)

    verifier = input("Enter the verifier token:")

    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }

    oauth = OAuth1(consumer_key,
                   consumer_secret,
                   request_key,
                   request_secret,
                   verifier=verifier
                   )

    res = requests.post(
        url='https://api.twitter.com/oauth/access_token', auth=oauth)
    credentials = parse_qs(res.text)
    access_token_key = credentials.get('oauth_token')[0]
    access_token_secret = credentials.get('oauth_token_secret')[0]

    api = TwitterAPI(consumer_key,
                     consumer_secret,
                     access_token_key,
                     access_token_secret)

    tweet_text = input('Enter tweet message:')
    file = open(img_path, "rb")
    image_data = file.read()

    res = api.request('media/upload', None, {'media': image_data})

    if res.status_code == 200:
        print('Media uploaded')
    else:
        print('Upload failed: ', res.text)

    if res.status_code == 200:
        media_id = res.json()['media_id']
        res = api.request('statuses/update',
                          {'status': tweet_text, 'media_ids': media_id})
        if res.status_code == 200:
            print('Status upload successful.')
        else:
            print('Status upload failed:', res.text)

    # with requests.Session() as c:
    #     USERNAME = input('Enter your username:')
    #     PASSWORD = getpass('Enter your password:')
    #     login_data = {
    #             'oauth_token': request_key,
    #             'session[username_or_email]': USERNAME,
    #             'session[password]': PASSWORD,
    #             'id':'oauth_form'
    #     }
    #     data = c.get(authorization_url, headers=headers)
    #     # print(data.content)
    #     soup = BeautifulSoup(data.content, 'html5lib')
    #     login_data['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']
    #     # a_token = c.cookies['authenticity_token']
    #     # print (a_token)
    #     c.post(authorization_url, data=login_data, headers=headers)
    #     page = c.get('https://api.twitter.com/oauth/authorize')
    #     pprint(page.text)


if __name__ == '__main__':
    set_desktop_background(sys.argv[1])
