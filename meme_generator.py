#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse as arg
import os
import random
import json
from formats import *

parser = arg.ArgumentParser('Meme Generator')

parser.add_argument('--mode', default=0,
                    help='Choose from two modes 0-Command line 1-Interactive'
                    )

parser.add_argument('--format', default=None,
                    help='Enter the format type')
parser.add_argument('--image1', type=str, default=None,
                    help='Enter the image path for 1st image')
parser.add_argument('--image2', type=str, default=None,
                    help='Enter the image path for 2nd image')
parser.add_argument('--text1', type=str, default=None,
                    help='Enter text1')
parser.add_argument('--text2', type=str, default=None,
                    help='Enter text2')
parser.add_argument('--random', type=str, default=None,
                    help='Enter either True or False required for format-0'
                    )

args = parser.parse_args()


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
        print data['data'][random.randint(1,
                           num_of_images)]['description']


# Main Function

if __name__ == '__main__':
    if args.mode == '0':
        if args.format == '0':
            if args.random == 'True' or args.random == 'False':
                random_meme(args.random)
            else:
                print 'Empty or invalid arguments'

        if args.format == '1':
            if args.image1 is not None and args.text1 is not None:
                meme_generator_1(args.image1, args.text1)
            else:
                print 'Missing arguments'

        if args.format == '2':
            if args.image1 is not None and args.text1 is not None:
                meme_generator_2(args.image1, args.text1)
            else:
                print 'Missing arguments'

        if args.format == '3':
            if args.image1 is not None and args.text1 is not None \
                and args.text2 is not None:
                meme_generator_3(args.image1, args.text1, args.text2)
            else:
                print 'Missing arguments'

        if args.format == '4':
            if args.image1 is not None and args.text1 is not None \
                and args.image2 is not None and args.text2 is not None:
                meme_generator_4(args.image1, args.image2, args.text1,
                                 args.text2)
            else:
                print 'Missing arguments'

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
            meme_generator_1(img, top_text)

        if format == '2':
            img = input('Enter the image path: ')
            bottom_text = input('Input the bottom line here: ')
            meme_generator_2(img, bottom_text)

        if format == '3':
            img = input('Enter the image path: ')
            top_text = input('Input the top line here: ')
            bottom_text = input('Input the bottom line here: ')
            meme_generator_3(img, top_text, bottom_text)

        if format == '4':
            img1 = input('Enter image 1 path: ')
            img2 = input('Enter image 2 path: ')
            top_text = input('Input the top line here: ')
            bottom_text = input('Input the bottom line here: ')
meme_generator_4(img1, img2, top_text, bottom_text)
