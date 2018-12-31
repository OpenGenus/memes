import os
import sys
import ctypes # for windows

def set_desktop_background(img_path):
    platform = sys.platform

    if platform == 'win32':
        '''
        Windows32
        '''
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path , 0)

    elif platform == 'Darwin':
        '''
        Macintosh
        '''
        pass

    elif platform == 'linux' or platform == 'linux2':
        '''
        Linux
        '''
        sessionName = os.getenv("DESKTOP_SESSION")

        if sessionName == 'gnome':
            os.system("gsettings set org.gnome.desktop.background picture-uri file:" + img_path)

        elif sessionName == 'kde':
            pass

        elif sessionName == 'xfce':
            pass

        elif sessionName == 'i3':
            os.system("feh --bg-scale " + img_path)

if __name__ == '__main__':
    set_desktop_background(sys.argv[1])

