import os
import pygtrie as pygtrie
import json
from PIL import Image
from collections import defaultdict

l = pygtrie.CharTrie()
p = defaultdict(list)

with open('searchtrie.json') as f:
	l._root.__setstate__(json.load(f))

with open('searchdict.json') as f:
	p = json.load(f)

with open('index.json') as f:
	data = json.load(f)

img_idx = list()

inp = input('Enter search string : ')
inp = inp.split(' ')

for word in inp:
	word = word.lower()
	indices = sorted(l[word:])
	for idx in indices:
		img_idx += p[str(idx)]

print(img_idx)

for idx in img_idx:
	file = data["data"][idx]["location"]
	Image.open(file).show()
#print(sorted(l['Tyr':]))
#print(p[str(l['Tyrion'])]))

