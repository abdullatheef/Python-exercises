# a program center_align.py to center align all lines in the given file.
import re
import os
import sys

f=open(sys.argv[1],"r")
s=f.readlines()
a=[]
e=''
for i in s:
	a.append(len(i))
	print a
b=max(a)
for i in s: 
	c=len(i)
	d=(b-c)/2
	for j in range(d): 
		i.add(0," ") 
		print i

