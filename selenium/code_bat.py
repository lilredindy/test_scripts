import unittest
from selenium import webdriver
#import time


class code_bat(unittest.TestCase):
	driver = webdriver.Firefox()

	def setUp(self):
		#self.driver = webdriver.Firefox()
		codeBat.driver.implicitly_wait(10) # seconds

	def test_login(self):
		codeBat.driver.get("http://codingbat.com/")
		codeBat.do_login("shri.amin@gmail.com", "maverick")
		#print (type(codeBat.driver.page_source))
		#time.sleep(5)
		self.assertTrue(codeBat.is_logged_in())

	#@unittest.skip("")
	def test_if_make_tags_problem_completed(self):
		codeBat.driver.get("http://codingbat.com/python/String-1")
		codeBat.do_login("shri.amin@gmail.com", "maverick")

		is_done_elem = codeBat.driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[3]/img")
		is_done_elem_attr = is_done_elem.get_attribute("src")
		#print is_done_elem_attr
		self.assertTrue(is_done_elem_attr == "http://codingbat.com/c2.jpg")

	def tear_down(self):
		codeBat.driver.quit() 

	@staticmethod
	def is_logged_in():
		txt = "Logged in" 
		return (txt in codeBat.driver.page_source)

	@staticmethod
	def do_login(username, password):
		if (codeBat.is_logged_in()):
			return 
		else:
			username_field = codeBat.driver.find_element_by_css_selector("input[name=uname]")
			username_field.send_keys(username)
			password_field = codeBat.driver.find_element_by_css_selector("input[name=pw]")
			password_field = password_field.send_keys(password)
			login_btn = codeBat.driver.find_element_by_css_selector("input[name=dologin]")
			login_btn.click()
    

if __name__ == '__main__':
	unittest.main()
