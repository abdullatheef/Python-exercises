import tablib
f=open("test.csv",'r')
data = tablib.Dataset()
for i in f.read():
	data.append(i)
print data
