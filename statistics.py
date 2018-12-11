import os
import argparse

parser = argparse.ArgumentParser('Statistics')
parser.add_argument("--data", type=str, default=".", help="Enter directory path")
args = parser.parse_args()
print()

data_size = 0
images = 0
sub_dirs = 0

for root, dirs, files in os.walk(args.data):
	for item in files:
		if item.endswith(('.jpg', '.png', '.bmp', '.tif', '.gif')):
			images += 1
		fpath = os.path.join(root, item)
		data_size += os.path.getsize(fpath)
	for item in dirs:
		sub_dirs += 1

print('Number of images:', images)
print('Total data size:', data_size, 'bytes')
print('Number of sub folders:', sub_dirs)
