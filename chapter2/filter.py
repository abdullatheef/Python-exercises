#an implementation for filter using list comprehensions.

def even(x):
	return x%2==0
def filter(fn,list_a):
	return [x for x in list_a if even(x)==True]
print filter(even,range(10))
