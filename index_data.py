import os
import argparse as arg
import json
import time

currentpath = os.path.dirname(os.path.abspath(__file__))
indexpath = os.path.join(currentpath, 'index')

data = []
path = []
description = []
dirName = 'data'
for (subdir, dirs, files) in os.walk(dirName):
    for file in files:
        if file.endswith('.jpg'):
            if os.path.exists(subdir + os.sep + file.split('.')[0]
                              + '.json'):
                with open(subdir + os.sep + file.split('.')[0] + '.json'
                          ) as f:
                    desc = json.load(f)
                strr = desc[file.split('.')[0]]['description']

                # print(str)

                description.append(desc[file.split('.'
                                   )[0]]['description'])
                data.append(file)
                filepath = subdir + os.sep + file
                path.append(filepath)
            else:

                # print(file)

                description.append(subdir.split('\\')[-2])
                data.append(file)
                filepath = subdir + os.sep + file
                path.append(filepath)


cat = []
path_cat = []
description_cat=[]
def category_index():
  for (subdir, dirs, files) in os.walk(dirName):
    for file in files:
        if os.path.exists(subdir + os.sep + 'data.txt'):
            f = open(subdir + os.sep + 'data.txt', "r")
            m = f.read()
            description_cat.append(m)
            path_cat.append(subdir + os.sep + 'data.txt')
            cat.append(subdir.split('\\')[-1])

child_cat = []
parent = []

def heirarchy():

  for (subdir, dirs, files) in os.walk(dirName):
    for file in files:
        if os.path.exists(subdir + os.sep + 'data.txt'):
            f = open(subdir + os.sep + 'data.txt', "r")
            m = f.read()
            parent.append(subdir.split('\\')[-2])
            child_cat.append(subdir.split('\\')[-1])

category_index()
heirarchy()

with open(os.path.join(indexpath,'heirarchy.json'), 'w') as f:
    json.dump({'data': [{'parent': w, 'name': x}
              for (w, x) in zip(parent, child_cat)]}, f,
              sort_keys=False, indent=4, ensure_ascii=False)


with open(os.path.join(indexpath,'category_index.json'), 'w') as f:
    json.dump({'data': [{'name': w, 'description': x, 'location': y}
              for (w, x, y) in zip(cat, description_cat, path_cat)]}, f,
              sort_keys=False, indent=4, ensure_ascii=False)



with open(os.path.join(indexpath, 'index.json'), 'w') as f:
    json.dump({'data': [{'name': w, 'description': x, 'location': y}
              for (w, x, y) in zip(data, description, path)]}, f,
              sort_keys=False, indent=4, ensure_ascii=False)

updateTime = time.ctime(max(os.stat(root).st_mtime for root,_,_ in os.walk('.\\data')))

def UpdateMemeDb():
    with open(os.path.join(indexpath,'memedb.json')) as f:
        index=0
        memeData = json.load(f)
        for root,dirs,files in os.walk('.\\data'):
            for file in files:
                cur_file = os.path.join(root, file)
                if file.endswith("json"):
                    index+=1
                    with open(cur_file) as data_file:
                        data = json.loads(data_file.read())
                    for key in data:
                        desc = data[key]['description']
                    try:
                        memeExist = memeData[desc]
                    except:
                        memeData[desc] = [index]

    with open(os.path.join(indexpath,'memedb.json'), 'w') as f:
            json.dump(memeData, f, sort_keys=False, indent=4, ensure_ascii=False)

def start(force):
    try:
        with open(os.path.join(indexpath,'timestamp.json')) as f:
            data = json.load(f)
        if data['last-updated'] != updateTime or force==1:
            UpdateMemeDb()
            with open(os.path.join(indexpath,'timestamp.json'), 'w') as f:
                json.dump({'last-updated':updateTime}, f)
    except:
        with open(os.path.join(indexpath,'timestamp.json'), 'w') as f:
            json.dump({'last-updated':updateTime}, f)
        UpdateMemeDb()
