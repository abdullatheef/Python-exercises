#a function extsort to sort a list of files based on extension.

def extsort(name_list):
 a=[]
 b=[]
 for i in name_list:
  a.append(i.split("."))
 r=sorted(a,key=fn)
 for j in r:
  k=('.').join(j)
  b.append(k)
 return b
def fn(n):
 return n[-1]

print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
