# Program to create a zip file
import sys
import zipfile
dirt=sys.argv[1]
zip=zipfile.ZipFile(dirt,'w')
for i in range(2,len(sys.argv)):
	zip.write(sys.argv[i])	

