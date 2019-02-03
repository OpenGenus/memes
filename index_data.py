import os
import json

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

with open('heirarchy.json', 'w') as f:
    json.dump({'data': [{'parent': w, 'name': x}
              for (w, x) in zip(parent, child_cat)]}, f,
              sort_keys=False, indent=4, ensure_ascii=False)


with open('category_index.json', 'w') as f:
    json.dump({'data': [{'name': w, 'description': x, 'location': y}
              for (w, x, y) in zip(cat, description_cat, path_cat)]}, f,
              sort_keys=False, indent=4, ensure_ascii=False)



with open('index.json', 'w') as f:
    json.dump({'data': [{'name': w, 'description': x, 'location': y}
              for (w, x, y) in zip(data, description, path)]}, f,
              sort_keys=False, indent=4, ensure_ascii=False)
