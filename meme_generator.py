import argparse as arg
import os
import random
import json
from format1 import *
from format2 import *
from format3 import *
from format4 import *
from format5 import *
from preprocess import preprocessImages
import urllib.request

parser = arg.ArgumentParser('Meme Generator')

parser.add_argument('--mode', default=0, help='Choose from two modes: 0-Command line 1-Interactive 2-URL')

parser.add_argument('--url1', default=None, help='Enter URL for first image')
parser.add_argument('--url2', default=None, help='Enter URL for second image')
parser.add_argument('--format', default=None, help='Enter the format type')
parser.add_argument('--image1', type=str, default=None, help='Enter the image path for 1st image')
parser.add_argument('--image2', type=str, default=None, help='Enter the image path for 2nd image')
parser.add_argument('--text1', type=str, default=None, help='Enter text1')
parser.add_argument('--text2', type=str, default=None, help='Enter text2')
parser.add_argument('--random', type=str, default=None, help='Enter either True or False required for format-0')

args = parser.parse_args()

# Download image from URL.

def download(url, img_name):
    urllib.request.urlretrieve(url, img_name+".jpg")

# Generates random meme.

def random_meme(show='True'):
    with open('index.json') as f:
        data = json.load(f)
    num_of_images = len(data['data'])

    if show == 'True':
        random_idx = random.randint(1, num_of_images)
        folder = data['data'][random_idx]['location']
        Image.open(folder).show()
    else:
        print (data['data'][random.randint(1,
                           num_of_images)]['description'])


# Main Function

if __name__ == '__main__':
    if args.mode == '0':
        if args.format == '0':
            if args.random == 'True' or args.random == 'False':
                random_meme(args.random)
            else:
                print ('Empty or invalid arguments')

        if args.format == '1':
            if args.image1 is not None and args.text1 is not None:
                preprocessImages(args.image1)
                formatObj = Format1(args.image1, args.text1)
                formatObj.generate()
            else:
                print ('Missing arguments')

        if args.format == '2':
            if args.image1 is not None and args.text1 is not None:
                preprocessImages(args.image1)
                formatObj = Format2(args.image1, args.text1)
                formatObj.generate()
            else:
                print ('Missing arguments')

        if args.format == '3':
            if args.image1 is not None and args.text1 is not None \
                and args.text2 is not None:
                preprocessImages(args.image1)
                formatObj = Format3(args.image1, args.text1, args.text2)
                formatObj.generate()
            else:
                print ('Missing arguments')

        if args.format == '4':
            if args.image1 is not None and args.text1 is not None \
                and args.image2 is not None and args.text2 is not None:
                preprocessImages(args.image1)
                preprocessImages(args.image2)
                formatObj = Format4(args.image1, args.image2, args.text1, args.text2)
                formatObj.generate()
            else:
                print ('Missing arguments')

        if args.format == '5':
            if args.image1 is not None and args.text1 is not None \
                    and args.image2 is not None and args.text2 is not None:
                text_top = args.text1.split(',')
                text_bottom = args.text2.split(',')
                if text_top.__len__() > 2 or text_bottom.__len__() > 2:
                    print("Too many arguements")
                else:
                    preprocessImages(args.image1)
                    preprocessImages(args.image2)
                    if text_top.__len__() == 2 and text_bottom.__len__() == 1:
                        formatObj = Format5(image1_path=self.image1,
                                     image2_path=self.image2,
                                     text_individual1=text_top[0],
                                     text_individual2=text_top[1],
                                     top_text=None,
                                     bottom_text=text_bottom[0])
                        formatObj.generate()

                    elif text_top.__len__() == 1 and text_bottom.__len__() == 2:
                        formatObj = Format5(image1_path=args.image1,
                                     image2_path=args.image2,
                                     text_individual1=text_bottom[0],
                                     text_individual2=text_bottom[1],
                                     top_text=text_top[0],
                                     bottom_text=None)
                        formatObj.generate()
                    else:
                        print("Missing arguements")
            else:
                print("Missing arguements")

    if args.mode == '1':
        if args.format is not None:
            format = args.format
        else:
            format = input('Enter the format type :')

        if format == '0':
            show = input('Generate random image? True/False:')
            random_meme(show)

        if format == '1':
            img = input('Enter the image path: ')
            top_text = input('Input the top line here: ')
            preprocessImages(img)
            formatObj = Format1(img, top_text)
            formatObj.generate()

        if format == '2':
            img = input('Enter the image path: ')
            bottom_text = input('Input the bottom line here: ')
            preprocessImages(img)
            formatObj = Format2(img, bottom_text)
            formatObj.generate()

        if format == '3':
            img = input('Enter the image path: ')
            top_text = input('Input the top line here: ')
            bottom_text = input('Input the bottom line here: ')
            preprocessImages(img)
            formatObj = Format3(img, top_text, bottom_text)
            formatObj.generate()

        if format == '4':
            img1 = input('Enter image 1 path: ')
            img2 = input('Enter image 2 path: ')
            top_text = input('Input the top line here: ')
            bottom_text = input('Input the bottom line here: ')
            preprocessImages(img1)
            preprocessImages(img2)
            formatObj = Format4(img1, img2, top_text, bottom_text)
            formatObj.generate()

        if format == '5':
            img1 = input('Enter image 1 path: ')
            img2 = input('Enter image 2 path: ')
            preprocessImages(img1)
            preprocessImages(img2)
            print(format5type1, format5type2)
            type = input('Select the layout of meme (default : 1): ')
            if type == '1' or type == '':
                top_text = input('Input the top spreading text: ')
                text1 = input('Input the line for first image: ')
                text2 = input('Input the line for second image: ')
                formatObj = Format5(image1_path=img1,
                             image2_path=img2,
                             text_individual1=text1,
                             text_individual2=text2,
                             top_text=top_text,
                             bottom_text=None)
                formatObj.generate()
            elif type == '2':
                text1 = input('Input the line for first image: ')
                text2 = input('Input the line for second image: ')
                bottom_text = input('Input the bottom spreading line: ')
                formatObj = Format5(image1_path=img1,
                             image2_path=img2,
                             text_individual1=text1,
                             text_individual2=text2,
                             top_text=None,
                             bottom_text=bottom_text)
                formatObj.generate()

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
            top_text = input('Input the top line here: ')
            preprocessImages(img)
            formatObj = Format1(img, top_text)
            formatObj.generate()

        if format == '2':
            if args.url1 is not None:
                url = args.url1
            else:
                url = input('Enter image URL: ')
            download(url, 'meme_img')
            img = 'meme_img.jpg'
            bottom_text = input('Input the bottom line here: ')
            preprocessImages(img)
            formatObj = Format2(img, bottom_text)
            formatObj.generate()

        if format == '3':
            if args.url1 is not None:
                url = args.url1
            else:
                url = input('Enter image URL: ')
            download(url, 'meme_img')
            img = 'meme_img.jpg'
            top_text = input('Input the top line here: ')
            bottom_text = input('Input the bottom line here: ')
            preprocessImages(img)
            formatObj = Format3(img, top_text, bottom_text)
            formatObj.generate()

        if format == '4':
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
            formatObj = Format4(img1, img2, top_text, bottom_text)
            formatObj.generate()

        if format == '5':
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

            print(format5type1, format5type2)
            type = input('Select the layout of meme (default : 1): ')

            if type == '1' or type == '':
                top_text = input('Input the top spreading text: ')
                text1 = input('Input the line for first image: ')
                text2 = input('Input the line for second image: ')
                formatObj = Format5(image1_path=img1,
                             image2_path=img2,
                             text_individual1=text1,
                             text_individual2=text2,
                             top_text=top_text,
                             bottom_text=None)
                formatObj.generate()
            elif type == '2':
                text1 = input('Input the line for first image: ')
                text2 = input('Input the line for second image: ')
                bottom_text = input('Input the bottom spreading line: ')
                formatObj = Format5(image1_path=img1,
                             image2_path=img2,
                             text_individual1=text1,
                             text_individual2=text2,
                             top_text=None,
                             bottom_text=bottom_text)
                formatObj.generate()
