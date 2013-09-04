#a program that works like wrap.py, but breaks the line only at the word boundaries

import sys


f=open(sys.argv[1],'r')
s=f.readlines()
a=''
for i in s:
 k=i.split()
 print"\n"
 for j in k:
  if len(a)<30:
   a=a+j+' '
  else:
   print a
   a=''

