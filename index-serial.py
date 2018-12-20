import os
import pygtrie as pygtrie
import json
from collections import defaultdict

t = pygtrie.CharTrie()
cnt=0

with open('index.json') as f:
	data = json.load(f)
x = len(data['data'])
m = defaultdict(list)

for i in range(0,x):
	desc = data['data'][i]['description'].split(' ')
	for words in desc:
		if(t.has_key(words)):
			m[t[words]].append(i)
			continue
		else:
			t[words] = cnt
			m[t[words]].append(i)
			cnt+=1		
print(m)

with open('searchtrie.json', 'w') as f:
	json.dump(t._root.__getstate__(),f,indent=2)
with open('searchdict.json', 'w') as f:
	json.dump(m,f,indent=2)

'''
l = pygtrie.CharTrie()
p = defaultdict(list)
with open('searchtrie.json') as f:
	l._root.__setstate__(json.load(f))
with open('searchdict.json') as f:
	p = json.load(f)

print(l['Tyrion'])
print(p[str(l['Tyrion'])])
'''
