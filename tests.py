########################
######## TESTS #########
########################

# Diagnostics for project
from termcolor import *
import colorama
import index_data
import time
import os
import meme_generator
import searchp
import preprocess
import recommendation
import logo

def cleanup():
	try:
		for file in os.listdir('./'):
			if file.endswith('.png') or file.endswith('.jpg'):
				os.remove(file)
		success()
		print(currentTime(), '# Cleanup Success ')
	except:
		failed()
		print(currentTime(), 'Cleanup Failed')

def success():
	cprint('# Success | ', 'green'),

def failed():
	cprint('> Failed | ', 'red'),

def currentTime():
	return time.ctime()

def checkGeneration(args):
	args.generate=1
	args.mode = '0'
	args.image1 = '.\\data\\got_memes\\images\\got01.jpg'
	args.image2 = '.\\data\\got_memes\\images\\got02.jpg'
	args.text1 = 'text 1'
	args.text2 = 'text 2'

	try:
		args.format = '1'
		meme_generator.start(args)
		success()
		print(currentTime(), 'Generation using format 1')
		print(' \t + Meme Generated using format 1')
	except:
		failed()
		print(currentTime(), 'Generation using format 1')
		print(' \t + Resolve errors - meme_generator.py [start], formats/Format1')

	try:
		args.format = '2'
		meme_generator.start(args)
		success()
		print(currentTime(), 'Generation using format 2')
		print(' \t + Meme Generated using format 2')
	except:
		failed()
		print(currentTime(), 'Generation using format 2')
		print(' \t + Resolve errors - meme_generator.py [start], formats/Format2')

	try:
		args.format = '3'
		meme_generator.start(args)
		success()
		print(currentTime(), 'Generation using format 3')
		print(' \t + Meme Generated using format 3')
	except:
		failed()
		print(currentTime(), 'Generation using format 3')
		print(' \t + Resolve errors - meme_generator.py [start], formats/format3')

def checkPreprocess(args):
	args.width = 600
	args.data = '.\\data'

	try:
		preprocess.start(args)
		success()
		print(currentTime(), 'Preprocessing')
		print(' \t + Preprocessing files from .\\data directory')
	except:
		failed()
		print(' \t + Preprocessing failed')
def checkRecommendations(args):
	# Checks for recommendation service
	args.recommend=1
	# Check with args.meme as path
	try:
		args.meme = '.\\data\\got_memes\\images\\got01.jpg'
		recommendation.start(args.meme)
		success()
		print(currentTime(), 'Recommendations for meme with path')
		print(' \t + Recommendations generated \n')
	except:
		failed()
		print(currentTime(), 'Recommendations for meme with path')
		print(' \t + Resolve errors - Recommendation.py [*]\n')

	# Check with args.meme as string
	try:
		args.meme = 'tyrion'
		recommendation.start(args.meme)
		success()
		print(currentTime(), 'Recommendations for meme with string')
		print(' \t + Recommendations generated\n')
	except:
		failed()
		print(currentTime(), 'Recommendations for meme with string\n')
		print(' \t + Resolve errors - Recommendation.py [*]\n')

def checkSearch(args):
	#Checking keyword based searching
	try:
		args.search=1
		args.mode='0'
		args.search_str = 'tyrion'
		args.index_search = 0
		searchp.start(args)
		success()
		print(currentTime(), 'Search with mode 0 , keyword Tyrion')
		print(' \t + Photo displayed\n')
	except:
		failed()
		print(currentTime(), 'Search with mode 0, keyword Tyrion')
		print(" \t + Resolve errors - search.py [start() & str_search ]\n")

	# Checking index based searching
	try:
		args.search=1
		args.mode='0'
		args.search_str = None
		args.index_search = 1
		args.search_idx = [1]
		searchp.start(args)
		success()
		print(currentTime(), "--> Search with mode 0 , index value 1")
		print(" \t + Photo displayed\n")
	except:
		failed()
		print(currentTime(), 'Search with mode 0, index_search with value 1')
		print(' \t + Resolve errors - search.py [start() & idx_search ]\n')

def checkIndexing(args):
	# Checking Index data procedure with force_index option enabled
	args.force_index=1
	try:
		index_data.start(args.force_index)
		success()
		print(currentTime(), 'Indexing\n')
	except:
		failed()
		print(currentTime(), 'Indexing')
		print(" \t + Resolve errors - index_data.py [start()] \n")

def start(args):
	logo.test_logo()
	print(args.module)
	if args.module == 'indexing' or args.module==None:
		checkIndexing(args)
	if args.module == 'search' or args.module==None:
		checkSearch(args)
	if args.module == 'recommend' or args.module==None:
		checkRecommendations(args)
	if args.module == 'generate' or args.module==None:
		checkGeneration(args)
	if args.module == 'preprocess' or args.module==None:
		checkPreprocess(args)
	cleanup()
