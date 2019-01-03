import os
import pygtrie as pygtrie
import json
import argparse as arg
from PIL import Image
from collections import defaultdict

parser = arg.ArgumentParser('searchp')

parser.add_argument('--mode', default=0, help='Choose from two modes: 0-Command line 1-Interactive')
parser.add_argument('--search_str', type=str, default=None, help='Enter search string: ')
parser.add_argument('--index_search', type=int, default=0, help='Choose 1 to enable searching images from their indices')
parser.add_argument('--search_idx', default=0, help='Enter image index: ')

args = parser.parse_args()

l = pygtrie.CharTrie()
p = defaultdict(list)

with open('searchtrie.json') as f:
	l._root.__setstate__(json.load(f))

with open('searchdict.json') as f:
	p = json.load(f)

with open('index.json') as f:
	data = json.load(f)

def str_search(inp):
	image_idx = list()
	inp = inp.split(' ')

	for word in inp:
		word = word.lower()
		indices = sorted(l[word:])

		for str_idx in indices:
			image_idx += p[str(str_idx)]

	#print(img_idx)

	for str_idx in image_idx:
		file = data["data"][str_idx]["location"]
		Image.open(file).show()

def idx_search(index):
	for idx in index:
		file = data["data"][int(idx)]["location"]
		Image.open(file).show()

#print(args.index_search)

if args.index_search == 0:
	if args.mode == '0':
		if args.search_str is not None:
			inp = args.search_str
			str_search(inp)
		else:
			print('Missing arguments')
	elif args.mode == '1':
		inp = input('Enter the search string: ')
		str_search(inp)
	else:
		print('Unknown arguments')

elif args.index_search == 1:

	if args.mode == '0':

		if args.search_idx is not None:
			index = args.search_idx
			idx_search(index)

		else:
			print('Missing arguments')

	elif args.mode == '1':
		index = input('Enter image index: ')
		idx_search(index)

	else:
		print('Unknown argument')			

else:
	print('Unknown argument')

#print(sorted(l['Tyr':]))
#print(p[str(l['Tyrion'])]))

