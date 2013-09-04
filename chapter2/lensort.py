#a function lensort to sort a list of strings based on length.

def lensort(list_a):
 list_a.sort(key=len)
 return list_a
print lensort(['ssasa','dsd','ssss'])
