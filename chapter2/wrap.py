#a program that takes filename and width as aruguments and wraps the lines longer than width.

import sys


f=open(sys.argv[1],'r')
s=f.readlines()
for i in s:
	if int(sys.argv[2])<len(i):
		print i[:int(sys.argv[2])]+"\n"+i[int(sys.argv[2]):]
