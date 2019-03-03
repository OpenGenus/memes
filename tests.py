########################
######## TESTS #########
########################

# Diagnostics for project
from termcolor import *
import colorama
import index_data
import time
import searchp
import recommendation
import logo

logo.test_logo()
def success():
	cprint('# Success | ', 'green'),
def failed():
	cprint('> Failed | ', 'red'),

def currentTime():
	return time.ctime()

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
	print()
	if args.module == 'indexing' or args.module==None:
		checkIndexing(args)
	if args.module == 'search' or args.module==None:
		checkSearch(args)
	if args.module == 'recommend' or args.module==None:
		checkRecommendations(args)
