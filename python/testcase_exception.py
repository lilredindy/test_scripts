import unittest
import math

class exceptionTestCase(unittest.TestCase):
	def runTest(self):
		"""runTest is method override of single test-case"""
		try:
			x = 0/2
		except ZeroDivisionError:
			pass
		else:
			self.fail("this is zero division error exception")


if __name__ == "__main__":
	unittest.main()