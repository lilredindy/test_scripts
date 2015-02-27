def foo():
	print "foo"

def bar():
	print "bar"

class XYZ():

	def __init__(self):
		self.x = foo()
		self.y = bar()

	def foobar(self):
		print "foobar"

xyz = XYZ()

xyz.foobar()
