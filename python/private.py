

class Foo(object):

	def __init__(self):
		pass


	#this is super-private (name-mangaling)
	def __bar(self):
		print "bar is super-private...get's name-mangaling...run-time error "

	def _bar(self):
		print "bar is semi-private...no run-time error"


f = Foo()
f.__bar()

