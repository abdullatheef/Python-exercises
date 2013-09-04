#a program to print each line of a file in reverse order.

import re
import os
import sys

f=open(sys.argv[1],'r')
s=f.readlines()
for i in s:
 j=i[::-1]
 print j

