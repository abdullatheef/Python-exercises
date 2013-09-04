# Program to list all the files in the given directory along with their length and last modification time

import os
import sys
dirt=sys.argv[1]
filenames=os.listdir(os.path.abspath(dirt))
print filenames
print 'filename\tLength\tLast modification'
for filename in filenames:
	print filename,'\t\t',len(open(os.path.abspath(dirt+'/'+filename)).readlines()),'\t',os.stat(os.path.abspath(dirt+'/'+filename))[8]

