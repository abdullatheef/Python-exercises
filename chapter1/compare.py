#to compare two strings

def istrcmp(a,b):
 a=a.lower()
 b=b.lower()
 if a==b:
  return True
 else:
  return False

print istrcmp('latheef','LATHeeF')
