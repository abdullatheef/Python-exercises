#Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively

import os
import sys


f=open(sys.argv[1],'r')
s=f.readlines()
if sys.argv[2]=='tail':
	print s[:11]
if sys.argv[2]=='head': 
	print s[-10:]
