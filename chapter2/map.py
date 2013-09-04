#an implementation for map using list comprehensions.

def square(x):
	return x*x
def map(fn,list_a):
	return [square(x) for x in list_a]
print map(square,range(5))
