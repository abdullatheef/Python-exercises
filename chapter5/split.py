# Program to split a file into different files of given length
import sys
n=sys.argv[1]
lines=open(sys.argv[2]).readlines()
i=0
def split(lines,i):
	filename='file%d'%i
	fp=open(filename,'a')
	if len(lines)>=3:
		for j in range(3):
			fp.write(lines[j])
		split(lines[3:],i+1)
	else:
		for j in range(len(lines)):
			fp.write(lines[j])
split(lines,i)
			
