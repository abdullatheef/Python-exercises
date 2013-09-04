#a program reverse.py to print lines of a file in reverse order.
#input file as command:eg..python program.py name.txt
import sys
import re
import os
import sys

f=open(sys.argv[1],'r')
s=f.readlines()
s.reverse()
print s


