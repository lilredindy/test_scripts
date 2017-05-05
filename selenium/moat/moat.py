#!/usr/bin/env python
#coding: utf8


import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time, traceback
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException

"""
Please write a small handful of Selenium tests in Python against
http://www.moat.com ( http://www.moat.com/ ):
1. Verify that the “Try These” links are random and that they work.
2. Verify that the “Recently Seen Ads” are no more than half an hour old.
3. Verify the ad count on the search result page is correct, even if there are
more than 100 ads in the result set.
4. Verify the “Share this Ad” feature
"""

import os
GECKO = ':/Users/shriamin/Development/test_tools/selenium'
os.environ['PATH'] += GECKO
print os.environ['PATH']

class moat(unittest.TestCase):

	def setUp(self): 
		#non-cloud code
		#chrome_path = "C:\\Documents and Settings\\chuck\Desktop\\shri\\Development\\test_tools\\selenium\\chromedriver.exe"
		self.driver = webdriver.Chrome() 
		#self.driver = webdriver.Firefox()
		#self.lib = moatLib(self.driver)  #library of useful methods
		self.driver.implicitly_wait(10) #waits for element to appear in DOM
		self.driver.set_page_load_timeout(10) #waits for page to fully load (readyState = true), but AJAX not included
		self.driver.get("http://www.moat.com/")
		

	def tearDown(self): 
		pass
		#self.driver.quit() 
		#self.driver.close() #only works with remote webdriver

	@classmethod
	def setUpClass(moat):
		pass

	@classmethod
	def tearDownClass(moat):
		pass

	@unittest.skip("")
	def test_scenario1(self) :
		#create python list of ad links
		L = []
		count = 3
		while (count > 0):
			self.driver.get("https://www.moat.com/")
			#self.driver.refresh()
			
			brands = [brand for brand in self.driver.find_element_by_css_selector("span.random-brand.hidden-xs").find_elements_by_tag_name("a")]		
			
			#STEP1: make sure of randomness
			for brand in brands:
				#self.assertFalse(list(set(X).intersection(set(e.text))))        
				self.assertTrue(brand.text not in L)
				L.append(str(brand.text)) #append new elements to master list
			print (L)
 
			#STEP2: validate the link works
			ad_text = brands[0].text
			brands[0].click() 
			self.assertTrue(self.driver.find_element_by_css_selector("span.page-type"))
			self.assertTrue(ad_text in self.driver.title)
			#self.assertTrue(ad_text in self.driver.page_source) 
			count -= 1 #decrement

	@unittest.skip("")
	def test_scenario2(self) :
		count = 3 
		while (count > 0):
			self.driver.get("https://www.moat.com/")
			E_text = [int(e.text.split()[0]) for e in self.driver.find_elements_by_css_selector("div.recently_seen_ads li.featured-agencies h4")]		
			#print (E_text)
			#E_text.append(35)
			self.assertFalse(any(e >= 30 for e in E_text))
			count -= 1 #decrement 

	@unittest.skip("")
	def test_scenario3(self) :
		#L = ["Blick", "Trump Hotels", "Bob Dylan"]
		L = ["Blick"]
		for search_str in L:
			self.driver.get("https://www.moat.com/")
			searchBar = self.driver.find_element_by_id("pro-landing-search-box")
			searchBar.send_keys(search_str)
			searchBar.submit()
			#self.driver.refresh() #refreshes to whatever driver.current_url is set to
			#validate next page
			time.sleep(5) #0 creatives is diplayed without sleep
			#wait = WebDriverWait(self.driver, 10)
			#wait.until(EC.title_is(search_str + " Creatives | Moat")) 
			print (self.driver.title)
			print (self.driver.current_url)

			counter = int(self.driver.find_element_by_css_selector("div.creative-count span.header-text").get_property('textContent').split()[0])
			print (counter)
			
			try:
				while (True):
					self.driver.find_element_by_css_selector("a.er-load-more").click()
					time.sleep(5) #what's the alternate solution, using waits perhaps
			except (ElementNotInteractableException, ElementNotVisibleException) as e:
				pass
			
			ads = self.driver.find_elements_by_css_selector("div.masonry-container > div") #
			print (len(ads))
			self.assertTrue(len(ads) == counter, "Ad count is: {},label displays: {}".format(len(ads), counter))

	def test_scenario4(self) :
		self.driver.get("https://www.moat.com/")
		searchBar = self.driver.find_element_by_id("pro-landing-search-box")
		searchBar.send_keys("Hotel")
		searchBar.submit()
		
		ad = self.driver.find_elements_by_css_selector("div.masonry-container > div")[0]

		'''
		signup_btn = self.driver.find_element_by_css_selector("a.signup-button")
		ActionChains(self.driver).context_click(signup_btn).perform()
		time.sleep(5)
		self.driver.save_screenshot("/Users/shriamin/Development/test_scripts/selenium/moat/ss.png")
		'''

		actions = ActionChains(self.driver)
		actions.move_to_element(ad)
		actions.perform()
		self.driver.save_screenshot("/Users/shriamin/Development/test_scripts/selenium/moat/ss.png")
		

if __name__ == '__main__':
	unittest.main()
