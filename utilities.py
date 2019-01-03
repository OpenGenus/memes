import os
import sys
import ctypes # for windows

# import for uploading images to imgur
from imgurpython import ImgurClient
from requests.exception import ConnectionError
def set_desktop_background(img_path):
    platform = sys.platform

    if platform == 'win32':
        '''
        Windows
        '''
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path , 0)

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
            os.system("gsettings set org.gnome.desktop.background picture-uri file:" + img_path)

        elif sessionName == 'kde':
            print('No support for KDE systems yet.')

        elif sessionName == 'xfce':
            print('No support for xfce systems yet.')

        elif sessionName == 'i3':
            os.system("feh --bg-scale " + img_path)

def upload_to_imgur(img_path):
    client_id = 'ad9097da8570318'
    client_secret = 'fec2165f7736d3b17d35b25e9bf168b9a3d8af15'

    try:
        client = ImgurClient(client_id, client_secret)
        response = client.upload_from_path(img_path)
    except ConnectionError:
        print('Check your internet connection.')
    else:
        print('Upload Successful!')
        print(response['link'])

if __name__ == '__main__':
    set_desktop_background(sys.argv[1])
