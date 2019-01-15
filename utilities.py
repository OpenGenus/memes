import os
import sys
import ctypes  # for windows
from getpass import getpass
from configparser import ConfigParser
import requests
from requests_oauthlib import OAuth1

# import for uploading images to imgur
from imgurpython import ImgurClient

# imports for twitterAPI
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

        imgur_username = input("Enter username:")
        imgur_password = getpass("Enter password:")

        login_data = {
            'username':imgur_username,
            'password':imgur_password
            }

        authorization_url = client.get_auth_url('pin')

        with requests.Session() as s:
            headers = {
                'user-agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
                }

            r = s.get(authorization_url, headers=headers)
            soup = BeautifulSoup(r.content, 'html5lib')

            login_data['allow'] = soup.find('button', attrs={'name':'allow'})['value']

            r = s.post(authorization_url, data=login_data, headers=headers)
            soup = BeautifulSoup(r.content, 'html5lib')
            pin = soup.find('input', attrs={'name':'pin'})['value']
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

    elif user_res.lower() == 'yes':
        try:
            response = client.upload_from_path(img_path)

        except Exception as e:
            print(e)

        else:
            print('Upload Successful! Check at', response['link'])


def upload_to_twitter(img_path):

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }

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

    with requests.Session() as s:
        USERNAME = input('Enter your username:')
        PASSWORD = getpass('Enter your password:')

        login_data = {
                'session[username_or_email]': USERNAME,
                'session[password]': PASSWORD,
                'form_id':'oauth_form'
        }

        r = s.get(authorization_url, headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')

        login_data['authenticity_token'] = soup.find('input', attrs={'name':'authenticity_token'})['value']

        r = s.post(authorization_url, data=login_data, headers=headers)

        soup = BeautifulSoup(r.content, 'html5lib')
        verifier = soup.findAll('code')[0].string


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


if __name__ == '__main__':
    set_desktop_background(sys.argv[1])
