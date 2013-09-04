# Program to find the number of python file in a directory recursively
import os
import sys
def countfiles(files):
	return [file for file in files if '.py' in file]
files=os.listdir(sys.argv[1])
pyfile=countfiles(files)
print len(pyfile)

	

	
