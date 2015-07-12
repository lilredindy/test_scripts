def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

my_get_text = p_decorate(get_text)

print my_get_text("John")

#$$#########################################
############################################
import string 

def get_message(msg_part):
	return "this is the message %s" % (msg_part)

def p_decorate(func):
	def func_wrapper(msg):
		msg = string.rstrip(msg, "lo")
		return func(msg)
	return func_wrapper

my_func_wrapper = p_decorate(get_message)
print my_func_wrapper("hello")


print "----------------------------------------------------"



class myDecorator(object):

    def __init__(self, f):
        print "inside myDecorator.__init__()"
        print f.__name__
        f() # Prove that function definition has completed

    def __call__(self):
        print "inside myDecorator.__call__()"


@myDecorator
def aFunction():
    print "inside aFunction()"


print "Finished decorating aFunction()"

aFunction()


print "----------------------------------------------------"


class entryExit():

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__

@entryExit
def func1():
    print "inside func1()"

@entryExit
def func2():
    print "inside func2()"

func1()
func2()

print "----------------------------------------------------"

def entryExit(s):
    def decorator(f): 
    	print "level 1"
        def new_f(*args):
        	print "level 2"
        	f(*args) 
        return new_f
    return decorator

@entryExit("foo")
def func1(s):
    print "%s func1()" % s

@entryExit("bar")
def func2(s):
    print "%s func2()" % s

print "level 3"
func1("hello")
print func1.__name__
func2("goodbye")
print func2.__name__
