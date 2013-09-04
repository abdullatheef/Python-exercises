#a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.

def index(list_a):
	a=[]
	for i in list_a:
		a.append(list_a.index(i))
	return a
def fn(list_b):
	return zip(index(list_b),list_b)
print fn(["a","b"])
 
