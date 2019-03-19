########################
####### BRIDGE #########
########################

# This acts as a bridge between the services and the launcher for the application

import argparse as arg
import sys
import logo
import recommendation
import index_data
import searchp
import preprocess
import meme_generator
import tests


if len(sys.argv)==1:
	logo.print_logo()
	print("Please refer to help section using openmemes --help / openmemes -h")

elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
	logo.print_logo()

parser = arg.ArgumentParser('bridge')

# Options for bridge #
parser.add_argument('--recommend', default=0, help='Generate recommendations')
parser.add_argument('--search', default=0, help='Search a photo')
parser.add_argument('--preprocess', default=0, help='Preprocessing Data')
parser.add_argument('--generate', default=0, help="Meme Generation service " )
parser.add_argument('--meme', type=str, default=None, help='Enter Image path or name for the meme')

## Indexing Services ##
parser.add_argument('--force_index', type=int, default=0, help="Enter 1 to force indexing")

## Searching Services ##
parser.add_argument('--mode', default=0, help='Choose from two modes: 0-Command line 1-Interactive (searchp) | 0-Command line 1-Interactive 2-URL (meme_generator)')
parser.add_argument('--search_str', type=str, default=None, help='Enter search string: ')
parser.add_argument('--index_search', type=int, default=0, help='Choose 1 to enable searching images from their indices ')
parser.add_argument('--search_idx', default=0, help='Enter image index: ')
parser.add_argument('--result', type=int, default=0,  help='Enter number of images to display: ')
parser.add_argument('--display_info', default=0, help='Enter result format 0-image(default) 1-text description: ')

## Preporcessing Services ##
parser.add_argument('--data', type=str, help='Enter image path (use with preprocess)',default='data')
parser.add_argument('--width', type=int, help='Enter width of image (use with preprocess)',default=600)

## Meme_generator Services ##
parser.add_argument('--url1', default=None, help='Enter URL for first image')
parser.add_argument('--url2', default=None, help='Enter URL for second image')
parser.add_argument('--format', default=None, help='Enter the format type')
parser.add_argument('--image1', type=str, default=None, help='Enter the image path for 1st image')
parser.add_argument('--image2', type=str, default=None, help='Enter the image path for 2nd image')
parser.add_argument('--text1', type=str, default=None, help='Enter text1')
parser.add_argument('--text2', type=str, default=None, help='Enter text2')
parser.add_argument('--random', type=str, default=None, help='Enter either True or False required for format-0')
parser.add_argument('--description', type=str, default='NewMeme', help='Enter description for meme')
parser.add_argument('--rating', type=int, default=0, help='Set a rating (1->5)')

## Test Services ##
parser.add_argument('--test',type=int, default=0, help='Set this to 1 for running a diagnostic')
parser.add_argument('--module', type=str, default=None, help='Enter module to run test')

args = parser.parse_args()

# This is the endpoint for setup to work and communicate to services
def cli():
	#uses command line args to invoke sevices
    if args.recommend:
        recommendation.start(args.meme)
    if args.force_index:
        index_data.start(args.force_index)
    if args.search:
        searchp.start(args)
    if args.preprocess:
        preprocess.start(args)
    if args.generate:
        meme_generator.start(args)
    if args.test:
        tests.start(args)
