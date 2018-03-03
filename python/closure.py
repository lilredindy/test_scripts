import time

'''
This question demonstrates a closure - a function that references one or more variables in its parent's scope. 
Here, the child function widget references the variable values, which was defined in the parent function factory. 
Even though factory has returned, the widget function still holds a reference to values and can read and write to it. 
We say that widget closes over values because it retains a reference to the values variable. 
This technique is valuable because it allows functions to have private state without objects or 
Object Oriented Programming. For example, we can use closures to create generator function (e.g., primeGenerator) 
or capture a partial function application (e.g., makeAdder).
'''

def factory():
    values = []
    def widget(value):
        values.append(value)
        return values
    return widget

worker = factory()
worker(1)
worker(2)
print worker(4)

doctor = factory()
doctor(1)
doctor(2)
print doctor(3)

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