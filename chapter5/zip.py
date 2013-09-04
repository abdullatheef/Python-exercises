# Program to implement itertools.izip()
n=0
def izip(l,p):
	i=0
	while i<len(l):
		yield l[i],p[i]	
		i=i+1
	
for i,j in izip(['a','b','c'],[1,2,3]):
	print i,j

