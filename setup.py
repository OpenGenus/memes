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
        'colorama',
        'simplejson',
        'numpy>=1.14.3' ,
        'PILLOW>=5.1.0',
        'imgurpython>=1.1.7',
        'requests>=2.21.0',
        'configparser>=3.5.0',
        'TwitterAPI>=2.5.8',
        'requests-oauthlib>=1.0.0',
        'facebook-sdk>=3.1.0',
        'pygtrie'
    ],
    entry_points={
        'console_scripts': [
            'openmemes=services.bridge:cli'
        ]
    },
)
