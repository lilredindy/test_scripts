import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

print('hello')

class HugsTestCase(unittest.TestCase):

	def setUp(self):
		print("hello world")
		capabilities = {"platform": "WINDOWS",
                 "browserName": "firefox",
                 "version": ""}
		self.driver = webdriver.Remote( 
   				command_executor='http://127.0.0.1:4444/wd/hub', 
   				desired_capabilities= capabilities )
		#NOTE: THE desired capabilities was set to WINDOWS but is now MAC
   		print self.driver.desired_capabilities

	def test_hello_world(self):
		print self.driver.session_id
		time.sleep(60)

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
		self.assertTrue("Hello, WorldS!" in self.driver.page_source)




	def tearDown(self):
		print("bye bye")
		self.driver.quit() 

if __name__ == '__main__':
	unittest.main()
