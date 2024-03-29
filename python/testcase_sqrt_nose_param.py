import unittest
import math
from nose_parameterized import parameterized,param
from nose.tools import *

class Foo():
	def new_sqrt(self, x):
		return math.sqrt(x)

class SquareRootTestCase(unittest.TestCase):

	def setUp(self):
		self.f = Foo()
		print "setup()"

	@parameterized.expand([(4,2),(9,3),(0,0),(100,10)])
	def test_sqrt(self, x, y):
		#assert(self.f.new_sqrt(x)  == y)
		#self.assertEquals(self.f.new_sqrt(x), y)
		assert_equal(self.f.new_sqrt(x), y)


	@parameterized.expand([ param(4,2),
							param(9,3),
							param(0,0),
							param(100,10)]	
    )
	def test_sqrt2(self, x, y):
		#assert(self.f.new_sqrt(x)  == y)
		#self.assertEquals(self.f.new_sqrt(x), y)
		assert_equal(self.f.new_sqrt(x), y)

	def data_src_func():
		l = [(4,2),(9,3),(0,0),(100,10)]
		return l

	@parameterized.expand(data_src_func)
	def test_sqrt3(self, x, y):
		#assert(self.f.new_sqrt(x)  == y)
		#self.assertEquals(self.f.new_sqrt(x), y)
		assert_equal(self.f.new_sqrt(x), y)


	def tearDown(self):
		print("teardown()")
		

if __name__ == '__main__':
	unittest.main()
