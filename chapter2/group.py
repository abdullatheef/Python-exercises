# Program to group lists in to a given size
def group(l,size):
 new=[]
 i=0
 while i<len(l):
  new.append(l[i:size+i])
  i=i+size
 return new
print 'Testing phase--Use integer list' 
n=raw_input("Enter the length of list:")
l=[]
for i in range(int(n)):
 l.append(int(raw_input("Enter the element %d:" % i)))
size=int(raw_input("Enter the size to group:"))
print 'Original list=',l
print 'group(',l,',',size,')=',group(l,size)

