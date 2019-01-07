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
    pass


if __name__ == '__main__':
    set_desktop_background(sys.argv[1])
