import argparse as arg
import os
import time
import json
from termcolor import *
import colorama
from index_data import invokeUpdate

colorama.init()
parser = arg.ArgumentParser('Recommendation')

parser.add_argument('--meme', type=str, default=None, help='Enter Image path for the meme')
parser.add_argument('--force_index', type=int, default=0, help="Enter 1 to force indexing")
args = parser.parse_args()
path = args.meme
force = args.force_index

#check for updates in the local directory
if force == 1:
    invokeUpdate(True)
def matchScore(first, second, secondPath, json_fail, descExist):
    score = 0
    #creating a match score based on common descriptions
    if (json_fail): # Both first and second are paths
        first = first.split('\\')
        second = second.split('\\')
    else: # second is a description and first may or may not be a description
        if descExist:
            first = first.split()
            second = second.split()
        else:
            first = first.split('\\')
            second = secondPath.split('\\')
    word_map = {}
    for word in first:
        try:
            word_map[word]+=1
        except:
            word_map[word]=0
    for word in second:
        try:
            exist = word_map[word]
            score = score + 1
        except:
            pass

    return score

def createRecommendations(final):
    memes_map = {}
    for item in final:
        try:
            memes_map[item[1]][0]+= 1
            try:
                check = meme_map[item[1]][1]
            except:
                if (item[2][-4::]!='json'):
                    memes_map[item[0]].append(item[2])
        except:
            memes_map[item[1]] = [item[0]]
            if (item[2][-4::]!='json'):
                memes_map[item[1]].append(item[2])

    recommended = []
    for key, value in memes_map.items():
        recommended.append(value)
    return recommended

def fileName(path):
    path = path[:path.rindex('.'):]
    name = path.split('\\')[-1]
    return name

image_name = fileName(path)

json_path = path[:path.rindex('.'):] + '.json' # Removing image extension and adding json to make path for json file

json_fail = False
# Trying to set description assuming json file exists for the Image
try:
    with open(json_path) as f:
        data = json.load(f)
        description = data[image_name]['description']

# Setting path as description if json is not present
except:
    description = path
    json_fail = True

# Now we have got the description to match with other images and create some Recommendations
final = []

for root, dirs, files in os.walk('.\\data'):
    for file in files:
        descExist = False
        cur_file = os.path.join(root, file)
        if file.endswith("json") and json_fail == False:
            with open(cur_file) as f:
                data = json.load(f)
                cur_description = data[fileName(cur_file)]['description']
                descExist = True

        elif file.endswith(("jpg", "jpeg", "png")):
            cur_description = os.path.join(root, file)
        else:
            continue
        score = matchScore(cur_description, description, path, json_fail, descExist)
        if(score > 0):
            final.append((score, fileName(file), cur_file))

recommended = createRecommendations(final)
recommended.sort(reverse=True) #based on score

# Indexing recommended memes

if(len(recommended))==0:
    cprint("\n** Sorry, We have no recommendations for you currently ** \n", 'red')
else:
    cprint("\n** We have generated some recommendations, have a look on these memes ** \n", 'green')
    cprint("Index \t Name \t\t\t Location \n", 'green')
    index=1
    for meme in recommended:
        if meme[1]!=path:
            print(index,' --> ', fileName(meme[1]), '\t', meme[1], '\n')
            index+=1
