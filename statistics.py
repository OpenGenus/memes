import os
import argparse
import math
from PIL import Image, ImageFont, ImageDraw

print()


#print(fileSizes)
#creates pie chart for fileSizes
def pieChart(display,fileSizes):
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

def main():
        parser = argparse.ArgumentParser('Statistics')
        parser.add_argument("--data", type=str, default=".", help="Enter directory path")
        parser.add_argument("--chart",type = str, help = 'Generates and saves a pie chart of sizes of each file format')

        args = parser.parse_args()
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
        if args.chart == "pie":
                pieChart(True,fileSizes)
        print()
        print('Number of images:', images)
        print('Total data size:', data_size, 'bytes')
        print('Number of sub folders:', sub_dirs)

if __name__ == "__main__":
        main()


