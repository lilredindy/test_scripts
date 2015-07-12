import unittest
import math
from nose_parameterized import parameterized

class Foo():
	def new_sqrt(self, x):
		return math.sqrt(x)

class SquareRootTestCase(unittest.TestCase):

	def setUp(self):
		self.f = Foo()
		print "setup()"

	@parameterized.expand([(4,2),(9,3),(0,0),(100,10)])
	def test_sqrt(self, x, y):
		assert(self.f.new_sqrt(x)  == y)

	def tearDown(self):
		print("teardown()")
		

if __name__ == '__main__':
	unittest.main()
