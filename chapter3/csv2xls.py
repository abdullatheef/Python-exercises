import sys
import tablib
def parse_csv(filename,d,c):
 return [x[:-1].split(d) for x in open(filename,'r').readlines() if x[0]!=c]
filename=sys.argv[1]
delim=raw_input("Enter the delimiter:")
comment=raw_input("Enter the comment indicator:")
parse_csv(filename,delim,comment)
data = tablib.Dataset()
for i in parse_csv(filename,delim,comment):
	data.append(i)
with open('test.xls', 'wb') as f:
	f.write(data.xls)



