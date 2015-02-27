

class Foo(object):

	def __init__(self):
		pass


	#this is super-private (name-mangaling)
	def __bar(self):
		print "bar is super-private...get's name-mangaling...run-time error "

	def _bar(self):
		print "bar is semi-private, no run-time error"

	def bar(self):
		print "bar is public, it works"

f = Foo()
f.bar()
f._bar()
#f.__bar()

