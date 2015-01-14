def foo():
	print "foo"

def bar():
	print "bar"

class XYZ():

	def __init__(self):
		self.x = foo()
		self.y = bar()


xyz = XYZ()

