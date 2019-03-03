########################
######## LOGO ##########
########################

from pyfiglet import figlet_format
from termcolor import *
import colorama

# This prints ascii art for the application
def print_logo():
    colorama.init()
    print()
    cprint(figlet_format('OPENGENUS', font='basic'), 'yellow')
    cprint(figlet_format('MEMES', font='starwars'), 'green')

def test_logo():
    colorama.init()
    print()
    cprint(figlet_format('TEST', font='basic'), 'red')
