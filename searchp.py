import os
import pygtrie as pygtrie
import json
import argparse as arg
from PIL import Image
from collections import defaultdict

parser = arg.ArgumentParser('searchp')

parser.add_argument('--mode', default=0, help='Choose from two modes: 0-Command line 1-Interactive')
parser.add_argument('--search_str', type=str, default=None, help='Enter search string: ')

args = parser.parse_args()

if args.mode == '0':
	if args.search_str is not None:
		inp = args.search_str
	else:
		print('Missing arguments')
elif args.mode == '1':
	inp = input('Enter the search string: ')
else:
	print('Unknown argument')	

l = pygtrie.CharTrie()
p = defaultdict(list)

with open('searchtrie.json') as f:
	l._root.__setstate__(json.load(f))

with open('searchdict.json') as f:
	p = json.load(f)

with open('index.json') as f:
	data = json.load(f)

img_idx = list()

inp = inp.split(' ')

for word in inp:
	word = word.lower()
	indices = sorted(l[word:])
	for idx in indices:
		img_idx += p[str(idx)]

#print(img_idx)

for idx in img_idx:
	file = data["data"][idx]["location"]
	Image.open(file).show()
#print(sorted(l['Tyr':]))
#print(p[str(l['Tyrion'])]))

