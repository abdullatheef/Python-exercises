# Program to list all files in a directory

import os
import sys
dirt=sys.argv[1]
filenames=os.listdir(os.path.abspath(dirt))
for filename in filenames:
	print filename
