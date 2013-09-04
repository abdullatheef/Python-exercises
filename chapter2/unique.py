#a function 'unique' to find all the unique elements of a list.

def unique(list_a):
	new_list=[]
	for i in list_a:
		if i not in new_list:
			new_list.append(i)
	return new_list
print unique([1,1,2,2,2,3])
#[1,2,3]
