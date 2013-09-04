#Cumulative product of a list [a, b, c, ...] is defined as [a, a*b, a*b*c, ...].

def cumulative_product(list_a):
	new_list=[]
	j=1
	for i in list_a:
		c=j*i
		new_list.append(c)
		j=c
	return new_list
print cumulative_product([1,2,3,4])

#24
