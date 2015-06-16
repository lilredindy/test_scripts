
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
Foo.fiction()
f.fact(6)
