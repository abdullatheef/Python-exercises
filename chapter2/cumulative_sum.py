#Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].

def cumulative_sum(list_a):
	new_list=[]
	j=0
	for i in list_a:
		c=j+i
		new_list.append(c)
		j=c
	return new_list
print cumulative_sum([1,2,3,4])

#10
