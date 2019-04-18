########################
######## TESTS #########
########################

# Diagnostics for project
from termcolor import *
import colorama
import time
import os
from . import index_data
from . import meme_generator
from . import searchp
from . import preprocess
from . import recommendation
from . import logo
from . import utilities

global failed_tests
global passed_tests
failed_tests = set([])
passed_tests = set([])
# Clean up routine
def cleanup():
	'''
	This function takes care of the garbage generated during the testing process
		# meme_generator --> Produces images that are not supposed to be in the directory after a test
	'''
	try:
		for file in os.listdir('./'):
			if file.endswith('.png') or file.endswith('.jpg'):
				os.remove(file)
		success()
		print(currentTime(), '# Cleanup Success ')
	except:
		failed()
		print(currentTime(), 'Cleanup Failed')

# Utility function for success message
def success():
	cprint('# Success | ', 'green'),

# Utility function for fail message
def failed():
	cprint('> Failed | ', 'red'),

# Utility function to generate timestamp for log of tests
def currentTime():
	return time.ctime()

# This funciton test the meme_generation procedures
def checkGeneration(args):
	'''
	Arguments that are common are set to some default values
		# generate -> 1 (useful for bridge service)
		# mode -> 0 (Non interactive mode)
		# image1, image2 -> Image paths (Set to arbitrary images)
		# text1, text2 -> Texts (Set to sample texts)
	'''
	global failed_tests
	global passed_tests
	args.generate=1
	args.mode = '0'
	args.image1 = '.' + os.sep + 'data' + os.sep + 'got_memes' + os.sep + 'images' + os.sep + 'got01.jpg'
	args.image2 = '.' + os.sep + 'data' + os.sep + 'got_memes' + os.sep + 'images' + os.sep + 'got02.jpg'
	args.text1 = 'text 1'
	args.text2 = 'text 2'
	args.description = 'newMeme'
	args.rating='0'

	try:
		args.format = '1'
		meme_generator.start(args)
		success()
		print(currentTime(), 'Generation using format 1')
		print(' \t + Meme Generated using format 1')
		passed_tests.add('Generate - Format1')

	except:
		failed()
		print(currentTime(), 'Generation using format 1')
		print(' \t + Resolve errors - meme_generator.py [start], formats/Format1')
		failed_tests.add('Generate - Format1')

	try:
		args.format = '2'
		meme_generator.start(args)
		success()
		print(currentTime(), 'Generation using format 2')
		print(' \t + Meme Generated using format 2')
		passed_tests.add('Generate - Format2')
	except:
		failed()
		print(currentTime(), 'Generation using format 2')
		print(' \t + Resolve errors - meme_generator.py [start], formats/Format2')
		failed_tests.add('Generate - Format2')

	try:
		args.format = '3'
		meme_generator.start(args)
		success()
		print(currentTime(), 'Generation using format 3')
		print(' \t + Meme Generated using format 3')
		passed_tests.add('Generate - Format3')
	except:
		failed()
		print(currentTime(), 'Generation using format 3')
		print(' \t + Resolve errors - meme_generator.py [start], formats/format3')
		failed_tests.add('Generate - Format3')

# Routine to check preprocessing service
def checkPreprocess(args):
	'''
	Default args are set to arbitrary values (can be changed)
		# width -> 600 (Default)
		# data -> directory for preprocessing (Set to ./data/got_memes/)
	'''
	args.width = 600
	args.data = '.' + os.sep + 'data' + os.sep + 'got_memes'

	try:
		preprocess.start(args)
		success()
		print(currentTime(), 'Preprocessing')
		print(' \t + Preprocessing files from .\\data\\got_memes directory')
		passed_tests.add('preprocess')
	except:
		failed()
		print(' \t + Preprocessing failed')
		failed_tests.add('preprocess')

# Routine to check recommendation service
def checkRecommendations(args):
	args.meme = '.' + os.sep + 'data' + os.sep + 'got_memes' + os.sep + 'images' + os.sep + 'got01.jpg'
	recommendation.start(args.meme)
	# Checks for recommendation service
	args.recommend=1
	# Check with args.meme as path
	try:
		args.meme = '.' + os.sep + 'data' + os.sep + 'got_memes' + os.sep + 'images' + os.sep + 'got01.jpg'
		recommendation.start(args.meme)
		success()
		print(currentTime(), 'Recommendations for meme with path')
		print(' \t + Recommendations generated \n')
		passed_tests.add('Recommendation - Path')
	except:
		failed()
		print(currentTime(), 'Recommendations for meme with path')
		print(' \t + Resolve errors - Recommendation.py [*]\n')
		failed_tests.add('Recommendation - Path')

	# Check with args.meme as string
	try:
		args.meme = 'tyrion'
		recommendation.start(args.meme)
		success()
		print(currentTime(), 'Recommendations for meme with string')
		print(' \t + Recommendations generated\n')
		passed_tests.add('Recommendation - String')
	except:
		failed()
		print(currentTime(), 'Recommendations for meme with string\n')
		print(' \t + Resolve errors - Recommendation.py [*]\n')
		failed_tests.add('Recommendation - String')

# Routine to check search service
def checkSearch(args):
	#Checking keyword based searching
	args.display_info = 0
	try:
		args.search=1
		args.mode='0'
		args.search_str = 'tyrion'
		args.index_search = 0
		searchp.start(args)
		success()
		print(currentTime(), 'Search with mode 0 , keyword Tyrion')
		print(' \t + Photo displayed\n')
		passed_tests.add('search - keyword')
	except:
		failed()
		print(currentTime(), 'Search with mode 0, keyword Tyrion')
		print(" \t + Resolve errors - search.py [start() & str_search ]\n")
		failed_tests.add('search - keyword')

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
		passed_tests.add('search - index')
	except:
		failed()
		print(currentTime(), 'Search with mode 0, index_search with value 1')
		print(' \t + Resolve errors - search.py [start() & idx_search ]\n')
		failed_tests.add('search - index')

# Routine to check indexing
def checkIndexing(args):
	# Checking Index data procedure with force_index option enabled
	args.force_index=1
	try:
		index_data.start(args.force_index)
		success()
		print(currentTime(), 'Indexing\n')
		passed_tests.add('Indexing')
	except:
		failed()
		print(currentTime(), 'Indexing')
		print(" \t + Resolve errors - index_data.py [start()] \n")
		failed_tests.add('Indexing')


def CheckImgAapi(args):
	path='.' + os.sep + 'data' + os.sep + 'got_memes' + os.sep + 'images' + os.sep + 'got01.jpg'
	try:
		utilities.tag_image(path)
		success()
		print(currentTime(),'Img_api')
		print(" \t + Image Tags Generated\n")
		passed_tests.add('Img_api')
	except:
		failed()
		print(currentTime(),'Img_api')
		print(" \t + Resolve errors - utilities.py [tag_image()] \n")
		failed_tests.add('Img_api')


# End point for test (Accessed by bridge)
def start(args):
	global passed_tests
	global failed_tests
	'''
	Checks are run in this order to avoid missing content and support other services
	'''
	logo.test_logo()
	print()
	if args.module == 'Img_api' or args.module==None:
		CheckImgAapi(args)
	if args.module == 'preprocess' or args.module==None:
		checkPreprocess(args)
	if args.module == 'indexing' or args.module==None:
		checkIndexing(args)
	if args.module == 'generate' or args.module==None:
		checkGeneration(args)
	if args.module == 'search' or args.module==None:
		checkSearch(args)
	if args.module == 'recommend' or args.module==None:
		checkRecommendations(args)
	cleanup()

	# Generating test report
	failedTests = len(failed_tests)
	passedTests = len(passed_tests)
	totalTests = failedTests + passedTests

	print()
	cprint('---- Test Report ---- ' + str(passedTests) + '/' + str(totalTests), 'yellow')
	cprint('Passed Tests ', 'green')
	for test in passed_tests:
		cprint(' + '+test, 'green')
	print()
	cprint('Failed Tests', 'red')
	for test in failed_tests:
		cprint(' - '+test, 'red')
