import time

def hand():
	print "hand"
	def foot():
		print "foot"
	return foot

hand()
print "bar"



import os

def here(basepath):
	print basepath
	def f(*path):
		print basepath
		return os.path.join(basepath, *path)
	return f

#here("/boo")
usr = here('foo/')
print dir(usr)
print usr.func_code
print usr('bin')