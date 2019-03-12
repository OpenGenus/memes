########################
### RECOMMENDATIONS ####
########################

import argparse as arg
import os
import time
import json
from termcolor import *
import colorama

colorama.init()

if os.sep == '\':
    seperation = '\\'
else:
    seperation = os.sep

# Procedure for generating a match score for two images
def matchScore(first, second, secondPath, json_fail, descExist):
    '''
    # Takes in certain arguments
        1- First --> First meme's path/description
        2- Second --> Second meme's path/description
        3- secondPath --> Path of second image in case description does not exist
        4- json_fail --> If first and second both are paths, this is set to True
        5- descExist --> Flag showing that description for meme exist or not
    '''
    score = 0
    #creating a match score based on common descriptions
    if (json_fail): # Both first and second are paths
        first = first.split(seperation)
        second = second.split(seperation)
    else: # second is a description and first may or may not be a description
        if descExist:
            first = first.split()
            second = second.split()
        else:
            first = first.split(seperation)
            second = secondPath.split(seperation)
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
    # Returns score of two image match

# This procedure generates a list of recommended memes based on their matchScore
def createRecommendations(final):
    # Takes in final (A list of items to form meme_map and fill recommendation list)
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

    #Returns recommendation list

# Returns name of file present on a path
def fileName(path):
    path = path[:path.rindex('.'):]
    name = path.split(seperation)[-1]
    return name

# This is the endpoint for recommend service
# It takes a path and from the image present on the meme,
# Uses matchScore and createRecommendations to present the list of recommendations to the user

def start(path):
    # Takes path of meme
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

    for root, dirs, files in os.walk('.' + seperation + 'data'):
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

        # Generating a list of recommended memes
