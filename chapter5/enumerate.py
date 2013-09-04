# Program to implement the built-in function enumerate()
import itertools
def my_enumerate(l):
	return itertools.izip(range(len(l)),l)
print list(my_enumerate(["a","b","c"]))
for i,c in my_enumerate(["a","b","c"]):
	print i,c 
