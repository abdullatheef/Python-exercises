# Program to to count number of files for each extension in the given directory

import sys
import os
def extcount(filenames):
	dict={}
	for filename in filenames:
		dict[filename.split('.')[1]]=dict.get(filename.split('.')[1],0)+1
	return dict
dirt=sys.argv[1]
filenames=os.listdir(os.path.abspath(dirt))
dict=extcount(filenames)
for k,v in dict.items():
	print v,k

