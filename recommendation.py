import argparse as arg
import os
import json
from termcolor import *
import colorama

colorama.init()
parser = arg.ArgumentParser('Recommendation')

parser.add_argument('--meme', type=str, default=None, help='Enter Image path for the meme')
args = parser.parse_args()
path = args.meme

def fileName(path):
    path = path[:path.rindex('.'):]
    name = path.split('\\')[-1]
    return name

image_name = fileName(path)

json_path = path[:path.rindex('.'):] + '.json' # Removing image extension and adding json to make path for json file

# Trying to set description assuming json file exists for the Image
try:
    with open(json_path) as f:
        data = json.load(f)
        description = data[image_name]['description']

# Setting Image name if json is not present
except:
    description = image_name

# Now we have got the description to match with other images and create some Recommendations
recommended = []

for root, dirs, files in os.walk('.\\data2'):
    for file in files:
        if file.endswith("json"):
            cur_file = os.path.join(root, file)
            with open(cur_file) as f:
                data = json.load(f)

                #print(data)
                #print(fileName(cur_file))
                cur_description = data[fileName(cur_file)]['description']
                #print('Checking ', cur_description, ' and ', description)
                if description in cur_description:
                    recommended.append((fileName(cur_file), cur_file))

# Indexing recommended memes
if(len(recommended))==0:
    cprint("\n** Sorry, We have no recommendations for you currently ** \n", 'red')
else:
    cprint("\n** We have generated some recommendations, have a look on these memes ** \n", 'green')
    cprint("Index \t Name \t\t\t Location \n", 'green')
    index=1
    for meme in recommended:
        print(index,' --> ', meme[0], '\t', meme[1], '\n')
        index+=1
