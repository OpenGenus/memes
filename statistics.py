import os
import argparse
import math
from PIL import Image, ImageFont, ImageDraw

parser = argparse.ArgumentParser('Statistics')
parser.add_argument("--data", type=str, default=".", help="Enter directory path")
args = parser.parse_args()
print()

data_size = 0
images = 0
sub_dirs = 0
fileSizes = {'.jpg':0,'.png':0,'.bmp':0,'.tif':0,'.gif':0}

for root, dirs, files in os.walk(args.data):
        for item in files:
                fpath = os.path.join(root, item)
                data_size += os.path.getsize(fpath)
                if item.endswith(('.jpg', '.png', '.bmp', '.tif', '.gif')):
                        images += 1
                
                #updates/creates the file sizes of the format of item
                dotIndex = -1
                for x in range(1,len(item)+1):
                        if item[-x] == '.':
                                dotIndex = len(item) - x
                                break
                if dotIndex >= 0 and item[dotIndex:] in fileSizes:
                        fileSizes[item[dotIndex:]] += os.path.getsize(fpath)
                elif dotIndex >= 0 and item[dotIndex:] not in fileSizes:
                        fileSizes[item[dotIndex:]] = os.path.getsize(fpath)

        for item in dirs:
                sub_dirs += 1

#creates pie chart for fileSizes
colorSequence = ["white","red","blue","green","yellow","brown","orange"]
total = sum(fileSizes.values())
size = 2000
image = Image.new("RGBA",(size,size),"#DDD")
draw = ImageDraw.Draw(image,image.mode)
currAngle = 0
count = 0              #for moving through colorSequence
font = ImageFont.truetype("calibri.ttf",size = 25)
magnitude = size/4

for formatName in fileSizes:
    if fileSizes[formatName] != 0:
        newAngle = (fileSizes[formatName]/total)*360
        draw.pieslice((0,0,size,size),currAngle,currAngle + newAngle, fill = colorSequence[count % 7])
        currAngle += newAngle
        count += 1

currAngle = 0
#labels the slices
for formatName in fileSizes:
    if fileSizes[formatName] != 0:
        newAngle = (fileSizes[formatName]/total)*360
        xCoord = int(size/2 + magnitude*math.cos(math.radians((currAngle + (newAngle+currAngle))/2)))#-5 accounts for length of text
        yCoord = int(size/2 + magnitude*math.sin(math.radians((currAngle + (newAngle+currAngle))/2)))
        print(formatName, xCoord, yCoord)
        if "{:0.2f}".format(100*fileSizes[formatName]/total) != "0.00":
                draw.text((xCoord,yCoord), formatName + " : {:0.2f}%".format(100*fileSizes[formatName]/total),"black",font = font)
        print(formatName + " : {:0.2f}%".format(100*fileSizes[formatName]/total))
        currAngle += newAngle
        magnitude += 50
        if magnitude > size/2:
            magnitude = size/4

del draw
image = image.resize((size//2,size//2))
image.show()

print('Number of images:', images)
print('Total data size:', data_size, 'bytes')
print('Number of sub folders:', sub_dirs)
