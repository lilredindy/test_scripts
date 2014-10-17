import unittest

print('hello')

class HelloWorldTestCase(unittest.TestCase):

	def setUp(self):
		print("hello world")

	def testHello1(self):
		self.assertFalse(True)

	def tearDown(self):
		print("bye bye")

if __name__ == '__main__':
	unittest.main()
