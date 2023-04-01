class knowledge():

	def cognize(self, obj):
		print (obj)


k = knowledge()
k.cognize("chariot")
k.cognize(k) 

class A ():

	def __init__(self, a):
		self.a = a

	@staticmethod
	def static_method():
		print ("nothing")

	def print_a_b(self, b):
		print (self.a)
		print (b)

a = A("asshole")
a.print_a_b("b")
A.static_method()
a.static_method()





