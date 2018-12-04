import os
import json

data = []
path = []
description = []
dirName = 'data'
for subdir, dirs, files in os.walk(dirName):
    
    for file in files:
        
        if file.endswith(".jpg"):

        	if os.path.exists(subdir + os.sep + file.split('.')[0] + '.json'): 
        		with open(subdir + os.sep + file.split('.')[0] + '.json') as f:
        			desc = json.load(f)
        		strr = desc[file.split('.')[0]]['description'] 	
        		#print(str)
        		description.append(desc[file.split('.')[0]]['description'])
        		data.append(file)
        		filepath = subdir + os.sep + file
        		path.append(filepath)

        		#print(file)
        	else:
        		description.append(subdir.split('\\')[-2])
        		data.append(file)
        		filepath = subdir + os.sep + file
        		path.append(filepath)
        			

with open('index.json', 'w') as f:
	json.dump({'data' : [{"name": w , "description": x , "location" : y} for w,x,y in zip(data,description,path)]},f,sort_keys = False, indent = 4, 
		ensure_ascii = False)
        
