import unittest

class Foo():
	list = []
	var = 10;

	def __init__(self):
		print('foo constructor')
		#self.var = 0
        #self.list = []

	def bar(self):
		print("this is bar")

	def star(self):
		print('this is star')


f1 = Foo()
print f1.var #class variable var, but you can use it with an instance???
print Foo().list
f1.list.append('a')
print (f1.list)

f2 = Foo()
print f2.var
f2.var = 12
print f2.var
print f1.var
f2.list.append('b')
print(Foo().list)

f2.list = ['c']
print(f2.list)
print(Foo().list)

f1.list = 'd'
f1.list2 = 'bob'
print f1.list2
print(f1.list)
print(Foo().list)
print(Foo.list)


#print(f2.list)
#print(f1.list)






'''
class HelloWorldTestCase(unittest.TestCase):

	def setUp (self):
		print ("setup")
		self.foo = Foo()

	def test1(self):
		print ("test 1")
		self.foo.list.append('a')
		print(self.foo.list)

	def test2(self):
		print ("test 2")
		self.foo.list.append('b')
		print(self.foo.list)


if __name__ == '__main__':
	unittest.main()
'''

