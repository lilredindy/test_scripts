
class Foo:

	def __init__(self, var = None):
		self.var = var

	@staticmethod
	def bar():
		print ("this is it " + self.var)


f = Foo("man")

f.bar()
