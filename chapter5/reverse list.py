# Program to iterate a list in reverse

class reverse_iter:
    def __init__(self, l):
        self.i = len(l)-1
        self.l = l

    def __iter__(self):
        return self

    def next(self):
        if self.i > 0:
            i = self.i
            self.i -= 1
            return l[i]
        else:
            raise StopIteration()
l=[1,2,3,4]
p=reverse_iter(l)
print p.next()

