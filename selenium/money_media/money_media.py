#!/usr/bin/env python
#coding: utf8

"""
Website: http://www.financialadvisoriq.com/
Username: qa-test@money-media.com
Password: money

Scenario1:
1. Login
2. Click on 'Finding and winning new clients' which is under ‘The topics à The Client’
3. Verify content is available

Scenario2:
1. Login
2. Type any keyword and click search
3. Verify search returns some content back
""" 

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time, traceback

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.common.exceptions import NoSuchElementException



class moneyMedia(unittest.TestCase):

	def setUp(self): 
		
		
		#non-cloud code
		#chrome_path = "C:\\Documents and Settings\\chuck\Desktop\\shri\\Development\\test_tools\\selenium\\chromedriver.exe"
		#self.driver = webdriver.Chrome(chrome_path) 
		self.driver = webdriver.Firefox()
		self.lib = moneyMediaLib(self.driver)
		self.driver.implicitly_wait(10) #waits for element to appear in DOM
		self.driver.get("http://www.financialadvisoriq.com/")
		

		'''		
		#browser stack code
		desired_cap = {'os': 'Windows', 'os_version': 'xp', 'browser': 'Firefox', 'browser_version': '35' }
		self.driver = webdriver.Remote(
    		command_executor='http://shriamin1:LsuuTUS1h1RQ3aNGtZus@hub.browserstack.com:80/wd/hub',
    		desired_capabilities=desired_cap)
		self.lib = moneyMediaLib(self.driver)
		self.driver.implicitly_wait(10) #waits for element to appear in DOM
		self.driver.get("http://www.financialadvisoriq.com/")
		'''

		'''
		#sauce labs code
		sauce_url = "http://shriamin:abf4b3e5-cfab-4a79-824c-08a4d4d843f9@ondemand.saucelabs.com:80/wd/hub"
		desired_capabilities = {
    		'platform': "Mac OS X 10.9",
    		'browserName': "chrome",
    		'version': "31",
		}
		self.driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=sauce_url)
		self.lib = moneyMediaLib(self.driver)
		self.driver.implicitly_wait(10)
		self.driver.get("http://www.financialadvisoriq.com/")
		'''

	def tearDown(self): 
		pass
		#self.driver.quit() 
		#self.driver.close() #only works with remote webdriver

	@classmethod
	def setUpClass(moneyMedia):
		pass

	@classmethod
	def tearDownClass(moneyMedia):
		pass

	@unittest.skip("")
	def test_scenario1(self) :
		self.lib.login("qa-test@money-media.com", "money")
		self.assertTrue(self.driver.find_element_by_css_selector("a[href='/logout']"))

		menu_link = self.driver.find_element_by_css_selector("#navigation > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
		hidden_menu_link1 = self.driver.find_element_by_css_selector("#navigation > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
		hidden_menu_link2 = self.driver.find_element_by_css_selector("#categoryDropdown_2881 > div:nth-child(1) > a:nth-child(1)")
		
		actions = ActionChains(self.driver) #moved to global scope
		actions.move_to_element(menu_link)
		actions.move_to_element(hidden_menu_link1)
		actions.click(hidden_menu_link2)
		actions.perform()

		url_str = "http://www.financialadvisoriq.com/category/2911"
		self.assertTrue(self.driver.current_url == url_str)
		self.assertTrue(self.driver.find_element_by_class_name("listing_links"))
		#txt = "The Client: Finding and winning new clients"
		#self.assertTrue(txt in self.driver.page_source)


	def test_scenario2(self):
		self.lib.login("qa-test@money-media.com", "money")
		self.assertTrue(self.driver.find_element_by_css_selector("a[href='/logout']"))
		self.lib.search("capitalism\n")
		#x,y coordinates are not 0,0 on sauce
		url_str = "http://www.financialadvisoriq.com/search/advanced?q=capitalism&x=0&y=0"
		self.assertTrue(self.driver.current_url == url_str)
		try:
			self.assertTrue(self.driver.find_element_by_class_name("reults"))
		except NoSuchElementException:
			self.driver.find_element_by_class_name("results")


	@unittest.skip("")
	def test_scenario3(self):
		self.lib.click_forgot_password_link()
		url_str = "http://www.financialadvisoriq.com/user/password"
		self.assertTrue(self.driver.current_url == url_str)

		
class moneyMediaLib():
	def __init__(self, driver):
		self.driver = driver

	def login(self, username, password):
		self.open_login_dialog()
		#self.driver.execute_script("document.getElementById('email').setAttribute('contentEditable','true')")
		#time.sleep(10)
		#wait = WebDriverWait(self.driver, 10)
		#WAIT FOR FORM ELEMENT TO BE PRESENT & VISIBLE
		#wait.until(EC.visibility_of_element_located((By.ID, "login_form")))
		#self.driver.find_element_by_id("email").send_keys(username)
		#self.driver.find_element_by_id("password").send_keys(password)
		self.driver.find_element_by_css_selector("div#popupContainer div#login_form form input#email").send_keys(username)
		self.driver.find_element_by_css_selector("div#popupContainer div#login_form form input#password").send_keys(password)
		self.driver.find_element_by_id("log_in").click()


	def search(self, text):
		#self.driver.find_element_by_css_selector("form#nav-search div.search-box input:nth-child(1)").send_keys(text)
		self.driver.find_element_by_css_selector("input[name=q]").send_keys(text)

	def click_forgot_password_link(self):
		self.open_login_dialog()
		self.driver.find_element_by_css_selector("#login_form > div.formFooter > div:nth-child(1) > a").click()

	def is_logged_in(self):
		txt = "Sign Out" 
		return (txt in self.driver.page_source)

	def open_login_dialog(self):
		if(self.is_logged_in()):
			return
		login_link = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/a")
		login_link.click()


if __name__ == '__main__':
	unittest.main()
