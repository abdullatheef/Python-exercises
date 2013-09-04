# Program to compute the total number of lines of code in all python files in the specified directory recursively.
import sys
import os
def pyfiles(files):
	for f in files:
		if '.py' in f:
			yield f
def printlines(pyfile):
	for f in pyfile:
		count=0
		for line in open(f).readlines():
			if line[0]!='#' and line!='\n':
				count=count+1
		print f,count
				
	

def main(dirt):		
	files=os.listdir(dirt)
	pyfile=pyfiles(files)
	printlines(pyfile)


main(sys.argv[1])
