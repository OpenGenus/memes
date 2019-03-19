########################
#### MEME GENERATOR ####
########################

# This service contains procedure to generate memes

import argparse as arg
import os
import random
import json
import sys
from formats.format1 import *
from formats.format2 import *
from formats.format3 import *
from preprocess import preprocessImages
import urllib.request
import logo

# This procedure uses formatObj to generate and show meme
def use(formatObj, args):
    meme_img = formatObj.generate()
    meme_with_logo = add_logo(meme_img)
    meme_with_logo.save(meme_with_logo.filename)
    path = meme_with_logo.filename.split(os.sep)

    fileName = path[-1].split('.')[0]

    # generating meta-data for memes based on args
    metaData = {}
    metaData[fileName] = {}
    metaData[fileName]['mode'] = args.mode
    metaData[fileName]['format'] = args.format
    metaData[fileName]['description'] = args.description
    metaData[fileName]['rating'] = args.rating

    if len(path) != 1:
        json_name = '.'+meme_with_logo.filename.split('.')[1] + '.json'
    else:
        json_name = meme_with_logo.filename.split('.')[0] + '.json'
    with open(json_name, 'w') as f:
        json.dump(metaData, f, indent=4)
    meme_with_logo.show()

#Includes Logo in Memes
def add_logo_opaque(image):
    logo = Image.open('logos/opengenus_logo.png')
    size= logo.size
    nimg = logo.resize((int(size[0]/4),int(size[1]/4)))
    n=image.size
    k=int((n[0]-int(size[0]/4)))
    g=int((n[1]-int(size[1]/4)))
    image.paste(nimg, ((k),(g)))
    return image

# Adds logo image and text to a meme
def add_logo(img):
    img = add_logo_img(img, 'logos/OpenGenus.png')
    img = add_logo_txt(img, 'OpenGenus')
    return img

# Procedure for adding logo image
def add_logo_img(meme_img, logo_img_path):
    logo_img = Image.open(logo_img_path)
    w, h = logo_img.size
    logo_img = logo_img.resize((int(w/2), int(h/2)), Image.ANTIALIAS)
    width, height = meme_img.size
    mbox = meme_img.getbbox()
    sbox = logo_img.getbbox()
    meme_logo = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    position = (mbox[2] - sbox[2] - 5, mbox[3] - sbox[3] - 30)
    meme_logo.paste(meme_img, (0, 0))
    meme_logo.paste(logo_img, position, mask=logo_img)
    meme_logo.filename = meme_img.filename[:-4]+'.png'
    return meme_logo

# Procedure for adding logo text
def add_logo_txt(meme_logo, txt):
    meme_logo_opengenus = Image.new('RGBA', meme_logo.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype('./impact/impact.ttf', 20)
    d = ImageDraw.Draw(meme_logo_opengenus)
    y = meme_logo.size[0] - 100
    x = meme_logo.size[1] - 35
    d.text((y, x), txt, font=fnt, fill=(255, 255, 255, 200))
    out_img = Image.alpha_composite(meme_logo, meme_logo_opengenus)
    out_img.filename = meme_logo.filename
    return out_img

# Utility function to download image from an address (URL)
def download(url, img_name):
    urllib.request.urlretrieve(url, img_name+".jpg")

# Generates random meme.
def random_meme(show='True'):
    with open('index.json') as f:
        data = json.load(f)
    num_of_images = len(data['data'])

    if show == 'True': # When show flag is set, the generated image is shown
        random_idx = random.randint(1, num_of_images)
        folder = data['data'][random_idx]['location']
        Image.open(folder).show()
    else: # When show flag is not set, Information about meme is printed
        print (data['data'][random.randint(1,
                           num_of_images)]['description'])


# Main Function
# End point of this service
def start(args):
    '''
    Generates meme with different arrangement of text and image based on arguments.
    # Mode - 0, 1
    # Formats
    '''

    formatObj = None
    if args.mode == '0':
        if args.format == '0':
            if args.random == 'True' or args.random == 'False':
                random_meme(args.random)
            else:
                print ('Empty or invalid arguments')

        if args.format == '1':
            if args.text1 and args.text2 and args.image1:
                preprocessImages(args.image1)
                formatObj = Format1(image_path=args.image1,
									top_text=args.text1,
									bottom_text=args.text2)
                use(formatObj, args)

            elif args.text1 and args.image1:
                preprocessImages(args.image1)
                formatObj = Format1(image_path=args.image1,
									top_text=args.text1,
                                    bottom_text=None)
                use(formatObj, args)

            elif args.text2 and args.image1:
                preprocessImages(args.image1)
                formatObj = Format1(image_path=args.image1,
									top_text=None,
									bottom_text=args.text2)
                use(formatObj, args)
            else:
                print('Missing arguments')

        if args.format == '2':
            if args.image1 is not None and args.text1 is not None \
                and args.image2 is not None and args.text2 is not None:
                preprocessImages(args.image1)
                preprocessImages(args.image2)
                formatObj = Format2(args.image1, args.image2, args.text1, args.text2)
                use(formatObj, args)
            else:
                print ('Missing arguments')

        if args.format == '3':
            if args.image1 is not None and args.text1 is not None \
                    and args.image2 is not None and args.text2 is not None:
                text_top = args.text1.split(',')
                text_bottom = args.text2.split(',')
                if text_top.__len__() > 2 or text_bottom.__len__() > 2:
                    print("Too many arguements")
                else:
                    preprocessImages(args.image1)
                    preprocessImages(args.image2)
                    formatObj = Format3(image1_path=args.image1,
										image2_path=args.image2,
										top_text=text_top,
										bottom_text=text_bottom)
                    use(formatObj, args)
            else:
                print("Missing arguements")

    if args.mode == '1':
        logo.print_logo()
        if args.format is not None:
            format = args.format
        else:
            format = input('Enter the format type :')

        if format == '0':
            show = input('Generate random image? True/False:')
            random_meme(show)

        if format == '1':
            img = input('Enter the image path: ')
            print(format1type1, format1type2, format1type3)
            user_res = input('Select one of the formats (default : 1): ')
            if user_res == '1':
                preprocessImages(img)
                top_text = input('Input the top line here: ')
                formatObj = Format1(image_path=img,
									top_text=top_text)
            elif user_res == '2':
                preprocessImages(img)
                bottom_text = input('Input the bottom line here: ')
                formatObj = Format1(image_path=img,
									bottom_text= bottom_text)
            elif user_res == '3':
                preprocessImages(img)
                top_text = input('Input the top line here: ')
                bottom_text = input('Input the bottom line here: ')
                formatObj = Format1(image_path=img,
									top_text=top_text,
									bottom_text=bottom_text)
            use(formatObj, args)

        if format == '2':
            img1 = input('Enter image 1 path: ')
            img2 = input('Enter image 2 path: ')
            top_text = input('Input the top line here: ')
            bottom_text = input('Input the bottom line here: ')
            preprocessImages(img1)
            preprocessImages(img2)
            formatObj = Format2(img1, img2, top_text, bottom_text)
            use(formatObj, args)

        if format == '3':
            img1 = input('Enter image 1 path: ')
            img2 = input('Enter image 2 path: ')
            preprocessImages(img1)
            preprocessImages(img2)
            print(format3type1, format3type2, format3type3, format3type4)
            type = input('Select the layout of meme (default : 1): ')

            top_text = list()
            bottom_text = list()

            if type == '1' or type == '':
                text1 = input('Input the top spreading text: ')
                text2 = input('Input the bottom spreading text: ')
                top_text.append(text1)
                bottom_text.append(text2)
                formatObj = Format3(image1_path=img1,
									image2_path=img2,
									top_text=top_text,
									bottom_text=bottom_text)
            elif type == '2':
                text1 = input('Input the top spreading text: ')
                text2 = input('Input the line for first image: ')
                text3 = input('Input the line for second image: ')
                top_text.append(text1)
                bottom_text.append(text2)
                bottom_text.append(text3)
                formatObj = Format3(image1_path=img1,
									image2_path=img2,
									top_text=top_text,
									bottom_text=bottom_text)
            elif type == '3':
                text1 = input('Input the line for first image: ')
                text2 = input('Input the line for second image: ')
                text3 = input('Input the bottom spreading line: ')
                top_text.append(text1)
                top_text.append(text2)
                bottom_text.append(text3)
                formatObj = Format3(image1_path=img1,
									image2_path=img2,
									top_text=top_text,
									bottom_text=bottom_text)
            elif type == '4':
                text1 = input('Input the top line for first image: ')
                text2 = input('Input the top line for second image: ')
                text3 = input('Input the bottom line for first image: ')
                text4 = input('Input the bottom line for second image: ')
                top_text.append(text1)
                top_text.append(text2)
                bottom_text.append(text3)
                bottom_text.append(text4)
                formatObj = Format3(image1_path=img1,
									image2_path=img2,
									top_text=top_text,
									bottom_text=bottom_text)
            use(formatObj, args)

    if args.mode == '2':
        if args.format is not None:
            format = args.format
        else:
            format = input('Enter the format type :')

        if format == '0':
            show = input('Generate random image? True/False:')
            random_meme(show)

        if format == '1':
            if args.url1 is not None:
                url = args.url1
            else:
                url = input('Enter image URL: ')
            download(url, 'meme_img')
            img = 'meme_img.jpg'
            print(format1type1, format1type2, format1type3)
            user_res = input('Select one of the formats (default : 1): ')

            if user_res == '1' or user_res == '':
                preprocessImages(img)
                top_text = input('Input the top line here: ')
                formatObj = Format1(image_path=img,
									top_text=top_text)
            elif user_res == '2':
                preprocessImages(img)
                bottom_text = input('Input the bottom line here: ')
                formatObj = Format1(image_path=img,
									bottom_text=top_text)
            elif user_res == '3':
                preprocessImages(img)
                top_text = input('Input the top line here: ')
                bottom_text = input('Input the bottom line here: ')
                formatObj = Format1(image_path=img,
									top_text=top_text,
									bottom_text=bottom_text)
            use(formatObj, args)

        if format == '2':
            if args.url1 is not None:
                url1 = args.url1
            else:
                url1 = input('Enter URL for first Image: ')
            if args.url2 is not None:
                url2 = args.url2
            else:
                url2 = input('Enter URL for second Image: ')
            download(url1, 'meme_img1')
            download(url2, 'meme_img2')
            img1 = 'meme_img1.jpg'
            img2 = 'meme_img2.jpg'
            top_text = input('Input the top line here: ')
            bottom_text = input('Input the bottom line here: ')
            preprocessImages(img1)
            preprocessImages(img2)
            formatObj = Format2(img1, img2, top_text, bottom_text)
            use(formatObj, args)

        if format == '3':
            if args.url1 is not None:
                url1 = args.url1
            else:
                url1 = input('Enter URL for first Image: ')
            if args.url2 is not None:
                url2 = args.url2
            else:
                url2 = input('Enter URL for second Image: ')
            download(url1, 'meme_img1')
            download(url2, 'meme_img2')
            img1 = 'meme_img1.jpg'
            img2 = 'meme_img2.jpg'

            print(format3type1, format3type2, format3type3, format3type4)
            type = input('Select the layout of meme (default : 1): ')

            top_text = list()
            bottom_text = list()

            if type == '1' or type == '':
                text1 = input('Input the top spreading text: ')
                text2 = input('Input the bottom spreading text: ')
                top_text.append(text1)
                bottom_text.append(text2)
                formatObj = Format3(image1_path=img1,
									image2_path=img2,
									top_text=top_text,
									bottom_text=bottom_text)
            elif type == '2':
                text1 = input('Input the top spreading text: ')
                text2 = input('Input the line for first image: ')
                text3 = input('Input the line for second image: ')
                top_text.append(text1)
                bottom_text.append(text2)
                bottom_text.append(text3)
                formatObj = Format3(image1_path=img1,
									image2_path=img2,
									top_text=top_text,
									bottom_text=bottom_text)
            elif type == '3':
                text1 = input('Input the line for first image: ')
                text2 = input('Input the line for second image: ')
                text3 = input('Input the bottom spreading line: ')
                top_text.append(text1)
                top_text.append(text2)
                bottom_text.append(text3)
                formatObj = Format3(image1_path=img1,
									image2_path=img2,
									top_text=top_text,
									bottom_text=bottom_text)
            elif type == '4':
                text1 = input('Input the top line for first image: ')
                text2 = input('Input the top line for second image: ')
                text3 = input('Input the bottom line for first image: ')
                text4 = input('Input the bottom line for second image: ')
                top_text.append(text1)
                top_text.append(text2)
                bottom_text.append(text3)
                bottom_text.append(text4)
                formatObj = Format3(image1_path=img1,
									image2_path=img2,
									top_text=top_text,
									bottom_text=bottom_text)
            use(formatObj, args)
            # Calls use function to generate and show images corresponging to formatObj generated
