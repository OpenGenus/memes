########################
###### PREPROCESS ######
########################

import os
from PIL import Image
import argparse as arg

#This perprocess images so that they can be consumed by other services
def preprocessImages(imagePath, imageWidth=600):
        # Takes in imagePath and imageWidth
        img = Image.open(imagePath)
        wpercent = imageWidth / float(img.size[0])
        hsize = int(float(img.size[1]) * float(wpercent))
        img = img.resize((imageWidth, hsize), Image.ANTIALIAS)
        img.convert('RGB').save(imagePath)
        # Image is saved after preprocessing

#This is the endpoint of preprocess service for the bridge
def start(args):
    # Revieves args from bridge to set the image basewidth and directory
    basewidth = args.width
    rootDir = args.data

    # Iterating through the images present and removing duplicates
    # and processing them using preprocessImages

    for (dirName, subdirList, fileList) in os.walk(rootDir):
        for fname in fileList:
            ext = os.path.splitext(fname)[-1].lower()
            if ext.endswith(('.jpg', '.png', '.bmp')):
                img = Image.open(dirName + '/' + fname)
                wpercent = basewidth / float(img.size[0])
                hsize = int(float(img.size[1]) * float(wpercent))
                img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                img.convert('RGB').save(dirName + '/'
                                        + os.path.splitext(fname)[0]
                                        + '.jpg')
                if ext.endswith(('.png', '.bmp')):  # remove duplicates
                    os.remove(dirName + '/' + fname)
