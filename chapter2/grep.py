#unix command command takes a string and a file as arguments and prints all lines in the file which contain the specified string.



import re
import os
import sys


f=open(sys.argv[1],'r')
s=f.readlines()
for i in s:
	if sys.argv[2] in i:
		print i
