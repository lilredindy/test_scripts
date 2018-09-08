def mk_default():
    print("mk_default has been called!")

def myfun(foo=mk_default()):
    print("myfun has been called.")

print("about to test functions")
myfun("testing")
myfun("testing again")



def foo(a=[]):
	a.append(5)
	return a

print foo([1])
print foo([2])
print foo([3])