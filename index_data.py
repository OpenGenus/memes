########################
###### INDEXING ########
########################

#This service contains procedure to generate indexes of certain data to be used by other services

import os
import argparse as arg
import json
import time

currentpath = os.path.dirname(os.path.abspath(__file__))
indexpath = os.path.join(currentpath, 'index')

# Separator detection to eliminate platform dependency
seperation = os.sep

dirName = 'data'


def is_image(file):
    return file.endswith('.png')or file.endswith('jpg') and file.startswith('meme')

def meme_index():
    data = []
    path = []
    description = []
    print(os.path.dirname(os.path.relpath(__file__)))
    for (subdir, dirs, files) in os.walk(dirName):
        for file in files:
            if is_image(file):
                if os.path.exists(subdir + os.sep + file.split('.')[0]
                                  + '.json'):
                    with open(subdir + os.sep + file.split('.')[0] + '.json'
                              ) as f:
                        desc = json.load(f)
                    strr = desc['description']

                    description.append(desc['description'])
                    data.append(file)
                    filepath = subdir + os.sep + file
                    path.append(filepath)

    with open(os.path.join(indexpath, 'index.json'), 'w') as f:
                json.dump({'data': [{'name': w, 'description': x, 'location': y}
                                    for (w, x, y) in zip(data, description, path)]}, f,
                          sort_keys=False, indent=4, ensure_ascii=False)
            # else:
            #
            #     # print(file)
            #     description.append(subdir.split('\\')[-2])
            #     data.append(file)
            #     filepath = subdir + os.sep + file
            #     path.append(filepath)



#Indexing data based on categories
def category_index():
  cat = []
  path_cat = []
  description_cat = []
  for (subdir, dirs, files) in os.walk(dirName):
    for file in files:
        if os.path.exists(subdir + os.sep + 'data.txt'):
            f = open(subdir + os.sep + 'data.txt', "r")
            m = f.read()
            description_cat.append(m)
            path_cat.append(subdir + os.sep + 'data.txt')
            cat.append(subdir.split(seperation)[-1])

    with open(os.path.join(indexpath, 'category_index.json'), 'w') as f:
        json.dump({'data': [{'name': w, 'description': x, 'location': y}
                            for (w, x, y) in zip(cat, description_cat, path_cat)]}, f,
                  sort_keys=False, indent=4, ensure_ascii=False)


def heirarchy():
    child_cat = []
    parent = []
    for (subdir, dirs, files) in os.walk(dirName):
        for file in files:
            if os.path.exists(subdir + os.sep + 'data.txt'):
                f = open(subdir + os.sep + 'data.txt', "r")
                m = f.read()
                parent.append(subdir.split(seperation)[-2])
                child_cat.append(subdir.split(seperation)[-1])

    with open(os.path.join(indexpath, 'heirarchy.json'), 'w') as f:
        json.dump({'data': [{'parent': w, 'name': x}
                            for (w, x) in zip(parent, child_cat)]}, f,
                  sort_keys=False, indent=4, ensure_ascii=False)




updateTime = time.ctime(max(os.stat(root).st_mtime for root,_,_ in os.walk(dirName)))

#This is the procedure to generate memedb json, that stores the meme data as json {meme_desc : index}
def UpdateMemeDb():
    # Walks through the data directory to update memedb
    # with open(os.path.join(indexpath,'memedb.json')) as f:
    index=0
    memeData ={}
    # memeData = json.load(f)
    for root,dirs,files in os.walk(dirName):
        for file in files:
            cur_file = os.path.join(root, file)
            if file.endswith("json"):
                index+=1
                with open(cur_file) as data_file:
                    data = json.loads(data_file.read())
                for key in data:
                    desc = data['description']
                try:
                    memeExist = memeData[desc]
                except:
                    memeData[desc] = [index]

    with open(os.path.join(indexpath,'memedb.json'), 'w') as f:
            json.dump(memeData, f, sort_keys=False, indent=4, ensure_ascii=False)



#This is the endpoint for force_index flag
#This forces openmemes to log changes with the use of timestamp
def start(force):
    # Takes force flag and based on flag value, memedb generation is managed
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


if __name__ == '__main__':
    meme_index()
    category_index()
    heirarchy()
