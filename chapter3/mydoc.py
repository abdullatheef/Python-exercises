# Program to implement pydoc

import sys
__import__(sys.argv[1])
print 'Help on module ',sys.argv[1]
print '\n\n\n DESCRIPTION \n\n\n'
print __import__(sys.argv[1]).__doc__
print '\n\n\n FUNCTIONS \n\n\n'
for i in dir(sys.argv[1]):
	print i+'()'
