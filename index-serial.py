import os
import pygtrie as pygtrie
import json
from collections import defaultdict

t = pygtrie.CharTrie()
currentpath = os.path.dirname(os.path.abspath(__file__))
indexpath = os.path.join(currentpath, 'index')
cnt=0

with open(os.path.join(indexpath,'index.json')) as f:
	data = json.load(f)
x = len(data['data'])
m = defaultdict(list)

for i in range(0,x):
	desc = data['data'][i]['description'].split(' ')
	for words in desc:
		words = words.lower()
		if(t.has_key(words)):
			m[t[words]].append(i)
			continue
		else:
			t[words] = cnt
			m[t[words]].append(i)
			cnt+=1
#print(m)

with open(os.path.join(indexpath,'searchtrie.json'), 'w') as f:
	json.dump(t._root.__getstate__(),f,indent=2)
with open(os.path.join(indexpath,'searchdict.json'), 'w') as f:
	json.dump(m,f,indent=2)

'''
Reloading the json files
l = pygtrie.CharTrie()
p = defaultdict(list)
with open('searchtrie.json') as f:
	l._root.__setstate__(json.load(f))
with open('searchdict.json') as f:
	p = json.load(f)

print(sorted(l['tyr':]))
print(p[str(l['tyrion'])])
'''
