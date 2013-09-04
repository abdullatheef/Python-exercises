# Program that takes URL of a webpage as argument and prints all the URLs linked from that webpage

import sys
import re
import urllib
url=sys.argv[1]
ufile = urllib.urlopen(url)
print 'Loading.....'
text=re.findall(r'http://[\S\s]+"',ufile.read())
for i in text:
	print i[:-1]

