from PIL import Image, ImageDraw, ImageFont
import textwrap
import argparse as arg
import numpy as np
import sys
import os, random
import json 
from pprint import pprint

parser = arg.ArgumentParser('Meme Generator')

parser.add_argument("--mode" , default = None , help="Choose from two modes 0-Command line 1-Interactive")

parser.add_argument("--format" , default = None , help="Enter the format type")
parser.add_argument("--image1", type = str , default = None , help="Enter the image path for 1st image")
parser.add_argument("--image2", type = str , default = None , help="Enter the image path for 2nd image")
parser.add_argument("--text1", type = str  , default = None , help="Enter text1")
parser.add_argument("--text2", type = str , default = None , help="Enter text2")
parser.add_argument("--random", type = str , default = None , help="Enter either True or False required for format-0")

args = parser.parse_args()

#random_image_generator
def random_meme(show = "True"):
    
    with open('index.json') as f:
            data = json.load(f)
    x = len(data['data'])

    if show == "True":
        randomIdx = random.randint(1, x)
        folder = data["data"][randomIdx]["location"]
        folder = os.sep.join(folder.split('/'))
        imgName = data["data"][randomIdx]["name"]
        file = folder + os.sep + imgName
        Image.open(file).show()
    else:
        
        print(data["data"][random.randint(1,x)]["description"])

#format-1 
def meme_generator_1(image_path, top_text, font_path='impact/impact.ttf', font_size=9):
    
    
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    image_width, image_height = img.size
    
    
    font = ImageFont.truetype(font = font_path, size = int(image_height*font_size)//100)
    
    
    top_text = top_text.upper()
    
    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width = chars_per_line)
    
    
    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x,y), line, fill='white', font=font)
        y += line_height
    img.save('meme-' + img.filename.split(os.sep)[-1])
    img.show()

#format-2
def meme_generator_2(image_path, bottom_text, font_path='impact/impact.ttf', font_size=9):
    
    
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    image_width, image_height = img.size
    
    
    font = ImageFont.truetype(font = font_path, size = int(image_height*font_size)//100)
    
    
    bottom_text = bottom_text.upper()

    
    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    bottom_lines = textwrap.wrap(bottom_text, width = chars_per_line)
    
    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x,y), line, fill='white', font=font)
        y += line_height

    img.save('meme-' + img.filename.split(os.sep)[-1])
    img.show()

#format-3
def meme_generator_3(image_path, top_text, bottom_text, font_path='impact/impact.ttf', font_size=9):
    
    
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    image_width, image_height = img.size
    
    
    font = ImageFont.truetype(font = font_path, size = int(image_height*font_size)//100)
    
    
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()

    
    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width = chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width = chars_per_line)
    
    
    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x,y), line, fill='white', font=font)
        y += line_height

   
    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x,y), line, fill='white', font=font)
        y += line_height

    img.save('meme-' + img.filename.split(os.sep)[-1])
    img.show()
#format-4
def meme_generator_4(image1_path, image2_path, top_text, bottom_text, font_path='impact/impact.ttf', font_size=9):
    
    
    img01 = Image.open(image1_path)
    img02 = Image.open(image2_path)
    images = map(Image.open, [image1_path, image2_path])

    size = 320,360
    img1 = img01.resize((320,360), Image.ANTIALIAS)
    img2 = img02.resize((320,360), Image.ANTIALIAS)
    img1.save("short1.jpg")
    img2.save("short2.jpg")
    images = map(Image.open, ["short1.jpg", "short2.jpg"])

    #widths, heights = zip(*(i.size for i in images))

    image_width = 640 #sum(widths)
    image_height = 360 #max(heights)

    img = Image.new('RGB', (image_width, image_height))

    x_offset = 0
    for im in images:
        img.paste(im, (x_offset, 0))
        x_offset += im.size[0]
    
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font = font_path, size = int(image_height*font_size)//100)
    
    
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()

    
    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width = chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width = chars_per_line)
    
    
    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x,y), line, fill='white', font=font)
        y += line_height

   
    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x,y), line, fill='white', font=font)
        y += line_height

    
    #img.save("meme3.jpg")
    img.save('meme-{}{}.jpg'.format(os.path.basename(image1_path).split('.')[0], os.path.basename(image2_path).split('.')[0]))
    img.show()
    

#main function
if __name__ == '__main__':
    if(args.mode == "0"):
        
        if(args.format == "0"):
            if(args.random == 'True' or args.random == 'False'):
                random_meme(args.random)    
            else:
                print('Empty or invalid arguments')

        if(args.format == "1"):
            if(args.image1 is not None and args.text1 is not None):
                meme_generator_1(args.image1, args.text1)
            else:
                print('Missing arguments')  

        if(args.format == "2"):
            if(args.image1 is not None and args.text1 is not None):
                meme_generator_2(args.image1, args.text1)
            else:
                print('Missing arguments')

        if(args.format == "3"):
            if(args.image1 is not None and args.text1 is not None and args.text2 is not None):
                meme_generator_3(args.image1, args.text1, args.text2)
            else:
                print('Missing arguments')

        if(args.format == "4"):
            if(args.image1 is not None and args.text1 is not None and args.image2 is not None and args.text2 is not None):
                meme_generator_4(args.image1, args.image2, args.text1, args.text2)
            else:
                print('Missing arguments')

    if(args.mode == "1"):
        
        if(args.format is not None):
            format = args.format
        else:
            format = input("Enter the format type :")

        if(format == "0"):
            show = input("Generate random image? True/False:")
            random_meme(show)

        if(format == "1"):
            img = input("Enter the image path: ")
            top_text = input("Input the top line here: ")
            meme_generator_1(img, top_text)

        if(format == "2"):
            img = input("Enter the image path: ")
            bottom_text = input("Input the bottom line here: ")
            meme_generator_2(img, bottom_text)

        if(format == "3"):
            img = input("Enter the image path: ")
            top_text = input("Input the top line here: ")
            bottom_text = input("Input the bottom line here: ")
            meme_generator_3(img, top_text, bottom_text)

        if(format == "4"):
            img1 = input("Enter image 1 path: ")
            img2 = input("Enter image 2 path: ")
            top_text = input("Input the top line here: ")
            bottom_text = input("Input the bottom line here: ")
            meme_generator_4(img1, img2, top_text, bottom_text)
