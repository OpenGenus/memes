########################
######## SETUP #########
########################

# This serves as an installer for openmemes

from setuptools import setup
#-e,--editable <path/url>
#Install a project in editable mode (i.e.  setuptools "develop mode") from a local project path.
setup(
    name="openmemes",
    version='1.0',
    py_modules=['bridge'],
    install_requires=[
        'argparse',
        'pyfiglet',
        'termcolor',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        openmemes=bridge:cli
    ''',
)
