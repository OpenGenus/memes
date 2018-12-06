import os
from PIL import Image 
import argparse as arg

parser = arg.ArgumentParser()
parser.add_argument('--data', type = str , help = "Enter image path", 
                    default = "data")
parser.add_argument('--width', type = int , help = "Enter width of image", 
                    default = 600)
args = parser.parse_args()
basewidth = args.width
rootDir = args.data

for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
                ext = os.path.splitext(fname)[-1].lower()
                if ext.endswith(('.jpg','.png','.bmp')):
                        img = Image.open(dirName + '/' + fname)
                        wpercent = (basewidth / float(img.size[0]))
                        hsize = int((float(img.size[1]) * float(wpercent)))
                        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                        img.convert('RGB').save(dirName + '/' + 
                                                os.path.splitext(fname)[0] + '.jpg')
                        if ext.endswith(('.png','.bmp')):   #remove duplicates
                            os.remove(dirName + '/' + fname)



