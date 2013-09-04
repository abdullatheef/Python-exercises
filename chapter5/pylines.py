# Program to compute the total number of lines of code in all python files in the specified directory recursively.
import sys
import os
def pyfiles(files):
	for f in files:
		if '.py' in f:
			print f,len(open(f).readlines())
	

def main(dirt):		
	files=os.listdir(dirt)
	pyfile=pyfiles(files)


main(sys.argv[1])

	
