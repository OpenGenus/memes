import os
import json

data = []
path = []
for subdir, dirs, files in os.walk('.'):
    for file in files:
        
        if file.endswith(".jpg"):
        	data.append(file)
        	filepath = subdir + os.sep + file
        	path.append(filepath)
        	#print(file)

with open('index.json', 'w') as f:
	json.dump({'data' : [{"description": "game of thrones" ,"name": data[y], "location" : path[y]} for y in range(0,len(path))]},f,sort_keys = True, indent = 4, 
		ensure_ascii = False)
        
