import unittest
from selenium import webdriver

print('hello')

class HugsTestCase(unittest.TestCase):

	def setUp(self):
		print("hello world")
		self.driver = webdriver.Firefox()

	def test_hello_world(self):
		# Go to codepad.org
		self.driver.get('http://codepad.org')
		 
		# Select the Python language option
		python_link = self.driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
		python_link.click()
		 
		# Enter some text!
		text_area = self.driver.find_element_by_id('textarea')
		text_area.send_keys("print 'Hello,' + ' World!'")
		 
		# Submit the form!
		submit_button = self.driver.find_element_by_name('submit')
		submit_button.click()
		 
		# Make this an actual test. 
		self.assertTrue(True)

	def tearDown(self):
		print("bye bye")
		self.driver.quit() 

if __name__ == '__main__':
	unittest.main()
