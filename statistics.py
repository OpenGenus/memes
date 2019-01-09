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
                extension = "." + str(os.path.splitext(item)[1][1:].strip().lower())
                #updates/creates the file sizes of the format of item
                if extension != ".":
                        #print(extension)
                        if extension in fileSizes:
                                fileSizes[extension] += os.path.getsize(fpath)
                        else:
                                fileSizes[extension] = os.path.getsize(fpath)
        for item in dirs:
                sub_dirs += 1

#print(fileSizes)
#creates pie chart for fileSizes
def pieChart(display):
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
        print()
        for formatName in fileSizes:
                if fileSizes[formatName] != 0:
                        newAngle = (fileSizes[formatName]/total)*360
                        xCoord = int(size/2 + magnitude*math.cos(math.radians((currAngle + (newAngle+currAngle))/2)))
                        yCoord = int(size/2 + magnitude*math.sin(math.radians((currAngle + (newAngle+currAngle))/2)))
                        #print(formatName, xCoord, yCoord)
                        if "{:0.2f}".format(100*fileSizes[formatName]/total) != "0.00":
                                draw.text((xCoord,yCoord), formatName + " : {:0.2f}%".format(100*fileSizes[formatName]/total),"black",font = font)
                        if display:
                                print(formatName + " : {:0.2f}%".format(100*fileSizes[formatName]/total))
                        currAngle += newAngle
                        magnitude += 50
                        if magnitude > size/2:
                                magnitude = size/4

        del draw
        image = image.resize((size//2,size//2))
        image.save('pieChart.png','PNG')
        if display:
                image.show()

print("Statistics\n----------")
while True:
        print("\n(1) Create and save pie chart with sizes of each file format")
        print("(2) Create, save, and print a pie chart with sizes of each file format")
        print("(3) Basic Statistical Data")
        print("(4) Exit")
        possibleChoices = ['1','2','3','4']
        answer = input("Please enter a number from above: ")
        while answer not in possibleChoices:
                answer = input("Invalid. Please enter a number from above: ")
        if answer == '1':
                pieChart(False)
        elif answer == '2':
                pieChart(True)
        elif answer == '3':
                print()
                print('Number of images:', images)
                print('Total data size:', data_size, 'bytes')
                print('Number of sub folders:', sub_dirs)
        elif answer == '4':
                break

