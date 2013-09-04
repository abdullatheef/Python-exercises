# Program to print lines in a file whose length is greater than 40
import sys
filenames=[]
for i in range(1,len(sys.argv)):
	filenames.append(sys.argv[i])	
def gen(filenames):
    for f in filenames:
        for line in open(f):
            if len(line)>40:
                print line
gen(filenames)


