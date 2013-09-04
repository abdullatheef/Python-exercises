# Program that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

import os
import sys

def findfile(dirt,dirt1):
	files=os.listdir(dirt)
	for f in files:
		print os.path.abspath(dirt+'/'+f)
		if os.path.isdir(os.path.abspath(dirt+'/'+f)) is True:
			if f==dirt1:
				print 'Directory found at ',os.path.abspath(dirt+'/'+dirt1)
			else:
				findfile(dirt+'/'+f,dirt1)
findfile('gh','findme')
		
			
