from pyfiglet import figlet_format
from termcolor import *
import colorama

def print_logo():
    colorama.init()
    print()
    cprint(figlet_format('OPENGENUS', font='basic'), 'yellow')

    cprint(figlet_format('MEMES', font='starwars'), 'green')
