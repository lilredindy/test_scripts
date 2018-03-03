import unittest
from selenium import webdriver
import sys
#import time


class code_bat(unittest.TestCase):

	driver = webdriver.Chrome()


	def setUp(self):
		#self.driver = webdriver.Firefox()
		code_bat.driver.implicitly_wait(10) # seconds

	def test_login(self):
		code_bat.driver.get("http://codingbat.com/")
		code_bat.do_login("shri.amin@gmail.com", "maverick")
		#print (type(code_bat.driver.page_source))
		#time.sleep(5)
		self.assertTrue(code_bat.is_logged_in())

	#@unittest.skip("")
	def test_if_make_tags_problem_completed(self):
		code_bat.driver.get("http://codingbat.com/python/String-1")
		code_bat.do_login("shri.amin@gmail.com", "maverick")

		is_done_elem = code_bat.driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[3]/img")
		is_done_elem_attr = is_done_elem.get_attribute("src")
		#print is_done_elem_attr
		self.assertTrue(is_done_elem_attr == "http://codingbat.com/c2.jpg")

	def tear_down(self):
		code_bat.driver.quit() 

	@staticmethod
	def is_logged_in():
		txt = "Logged in" 
		return (txt in code_bat.driver.page_source)

	@staticmethod
	def do_login(username, password):
		if (code_bat.is_logged_in()):
			return 
		else:
			username_field = code_bat.driver.find_element_by_css_selector("input[name=uname]")
			username_field.send_keys(username)
			password_field = code_bat.driver.find_element_by_css_selector("input[name=pw]")
			password_field = password_field.send_keys(password)
			login_btn = code_bat.driver.find_element_by_css_selector("input[name=dologin]")
			login_btn.click()
    

if __name__ == '__main__':
	unittest.main()
