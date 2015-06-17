# dumb recursive factorial
def g_func(a,b):
    a = a
    b = b
    c = a +b
    return c
    
print __name__
print g_func(2, 3)
print g_func.__doc__
print g_func.__name__
print g_func.__module__

class Foo:
    
    @classmethod
    def fiction(cls):
        print "ok"

    def fact(self, n):
        if n < 2:
            print "hell"
        else:
            print "not hell"
            n = n/2
            self.fact(n)
            
f = Foo()
print type(f)
print type(Foo)
Foo.fiction()
f.fact(6)
print f.fact.__doc__
print f.fact.__name__
print f.fact.__module__
