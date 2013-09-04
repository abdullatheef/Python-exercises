#   a function dups to find all duplicates in the list

def dups(list_a):
	newlist=[]
	newlist_a=[]
	for i in list_a:
		if i not in newlist:
			newlist.append(i)
		else:
			newlist_a.append(i)
	return newlist_a 
print dups([1,1,1,2,3,3,4,4])
 
