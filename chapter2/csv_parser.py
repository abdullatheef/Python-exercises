#csv parser to support any delimiter and comments.

def parse(a,b,c):
	return [i.strip().split(b) for i in open(a,'r').readlines() if not i.startswith(c)]
print parse('a.txt', '!', '#')
