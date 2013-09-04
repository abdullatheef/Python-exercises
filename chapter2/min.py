#implementation for min function in python
def mini(l):
	j=l[1]
	for i in l:
		if i<j:
			j=i
	return j
print mini([3,4,6,2,5,1,7])

#1
