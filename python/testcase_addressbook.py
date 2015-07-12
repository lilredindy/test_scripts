import unittest
import addressbook


class AddressBookTestCase(unittest.TestCase):

	def setUp(self):
		self.a = addressbook.AddressBook()
		print "---------------------------------------------------------------------------"

	def test_add_1(self):
		self.a.add_contact()
		assert self.a.count() == 1,'count should be %d' % self.a.count()

	def test_add_2(self):
		self.a.add_contact()
		self.a.add_contact()
		assert self.a.count() == 2, 'count should be %d' % self.a.count() 

	def test_add_0_delete_1(self):
		self.a.delete()
		assert self.a.count() == 0, 'count should be %d' % self.a.count()
	
	def test_add_1_delete_1(self):
		self.a.add_contact()
		self.a.delete()
		assert self.a.count() == 0, 'count should be %d' % self.a.count()
	
	def test_add_2_delete_1(self):
		self.a.add_contact()
		self.a.add_contact()
		self.a.delete()
		assert self.a.count() == 1, 'count should be %d' % self.a.count()

	def test_find(self):
		index = self.a.add_contact()
		assert self.a.find(index)

	def test2(self):
		y = 1
		assert y == 1, 'y is 1'



if __name__ == '__main__':	
	unittest.main()