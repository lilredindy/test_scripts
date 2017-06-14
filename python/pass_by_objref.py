def reassign(m):
	m = [1,2]
def append(m):
	m.append(1)

l = [0]
reassign(l)
print(l)
append(l)
print(l)


class callByRef:
    def __init__(self, **args):
        for (key, value) in args.items():
            setattr(self, key, value)

def func4(bargs):
    bargs.a = 'new-value'        # args is a mutable callByRef
    bargs.b = args.b + 1         # change object in-place
    bargs.c = "test"

args = callByRef(a='old-value', b=99)
func4(args)
print(args.a, args.b,args.c)