#!/usr/bin/env python
#coding: utf8


import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os, sys, time, traceback, random, re
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

class moat(unittest.TestCase):

	def setUp(self):
		try: 
			#non-cloud code
			#self.driver = webdriver.Chrome()
			self.driver = webdriver.Firefox()
			self.driver.implicitly_wait(5) #waits for element to appear in DOM
			self.driver.get("http://www.moat.com/")
		except Exception as e:
			self.driver.save_screenshot(os.getcwd() + os.path.sep + unittest.TestCase.id(self).split(".")[2] + ".png") 			
			self.fail(e)


	def tearDown(self): 
		self.driver.quit() 

	@classmethod
	def setUpClass(moat):
		pass

	@classmethod
	def tearDownClass(moat):
		pass

	#@unittest.skip("")
	def test_scenario1(self) :
		"""1. Verify that the “Try These” links are random and that they work."""
		try:
			L = {} 
			count = 5
			while (count):
				self.driver.get("https://www.moat.com/")
				brand_links = [brand for brand in self.driver.find_element_by_css_selector("span.random-brand.hidden-xs").find_elements_by_tag_name("a")]		
			
				for link in brand_links:
					if link.text not in L:
						L[link.text] = 1
					else:
						L[link.text] += 1   

				#validate link works
				retain_txt = brand_links[0].text #DOM destroyed after click
				brand_links[0].click() 
				ad_label = self.driver.find_element_by_css_selector("span.page-type")
				time.sleep(3) #ad_label is updated with AJAX
				self.assertEqual(ad_label.text, retain_txt) 
				self.assertTrue(retain_txt in self.driver.title)
				count -= 1 

			print (L)
			self.assertFalse(any(l > 2 for l in L.values()), "Try these links not random {}".format(L))

		except Exception as e:
			self.driver.save_screenshot(os.getcwd() + os.path.sep + unittest.TestCase.id(self).split(".")[2] + ".png") 			
			self.fail(e)


	#@unittest.skip("")
	def test_scenario2(self) :
		"2. Verify that the “Recently Seen Ads” are no more than half an hour old."
		try:
			count = 5
			while (count):
				self.driver.get("https://www.moat.com/")
				recent_ads = [recent_ad.text for recent_ad in self.driver.find_elements_by_css_selector("div.recently_seen_ads li.featured-agencies h4")]		
				#recent_ads.append("35 mins ago")
				self.assertFalse(any((int(recent_ad.split()[0]) >= 30) for recent_ad in recent_ads), "{}".format(recent_ads))
				count -= 1  
		except Exception as e:
			self.driver.save_screenshot(os.getcwd() + os.path.sep + unittest.TestCase.id(self).split(".")[2] + ".png") 			
			self.fail(e)		


	#@unittest.skip("")
	def test_scenario3(self) :
		"""3. Verify the ad count on the search result page is correct, 
		even if there aremore than 100 ads in the result set."""

		try:
			self.driver.get("https://www.moat.com/")
			searchBar = self.driver.find_element_by_id("pro-landing-search-box")
			
			search_list = ["Pabst Blue Ribbon", "KLM", "Bob Dylan", "New Yorker"]
			searchBar.send_keys(random.choice(search_list))
			searchBar.submit()
			
			time.sleep(5) #0 creatives, another AJAX issue 
			#print (self.driver.title)
			#print (self.driver.current_url)

			num_creatives = (self.driver.find_element_by_css_selector("div.creative-count span.header-text").get_property('textContent').split()[0])
			num_creatives = re.sub('[,]', '',num_creatives) #strip out the comma
			#print (num_creatives)

			while (True):
				try:
					self.driver.find_element_by_css_selector("div.full-screen-load-more-container.visible")	
				except Exception as e:
					break 	
				self.driver.find_element_by_css_selector("a.er-load-more").click()
				time.sleep(5) #wait for ajax to load thumbnails (not long enough for larger load)
		

			ads = self.driver.find_elements_by_css_selector("div.masonry-container > div") 
			self.assertEqual(len(ads), num_creatives, "Ad count is: {},label displays: {}".format(len(ads), int(num_creatives)))
		except Exception as e:
			self.driver.save_screenshot(os.getcwd() + os.path.sep + unittest.TestCase.id(self).split(".")[2] + ".png") 			
			self.fail(e)		

	#@unittest.skip("")
	def test_scenario4(self) :
		"""4. Verify the “Share this Ad” feature"""

		try:
			self.driver.get("https://www.moat.com/")
			searchBar = self.driver.find_element_by_id("pro-landing-search-box")
			searchBar.send_keys("Canon") #fix
			searchBar.submit()
			self.driver.find_elements_by_css_selector("div.masonry-container > div")[0].click()
			self.driver.find_element_by_link_text("Share").click()
			time.sleep(1)
			#print(len(self.driver.window_handles))
			
			share_popup_txt = self.driver.find_element_by_css_selector("div.popup div.popup-header span.header-text").text
			self.assertEqual(share_popup_txt, "Share")
			
			share_popup_close_btn = self.driver.find_element_by_css_selector("div.popup div.popup-header span.close-button img.close-popup-icon")

			share_popup_url_label_txt = self.driver.find_element_by_css_selector("div.popup div.popup-body span.url-label").text
			self.assertEqual(share_popup_url_label_txt, "Shareable URL")	

			self.driver.find_element_by_css_selector("div.popup div.popup-body img.url-share-icon")
			share_popup_url_input_box = self.driver.find_element_by_css_selector("div.popup div.popup-body div.url input.url-field")
			share_url = share_popup_url_input_box.get_attribute("value")
			static_url = "https://moat.com/creative/548af492583c784247090faef99de0cb?region=US" #fix
			self.assertEqual(static_url, share_url) #static test


			copy_btn = self.driver.find_element_by_css_selector("div.popup div.popup-body div.button-div button.copy-button")
			self.assertEqual(copy_btn.text, "Copy Link")
			copy_btn.click()
			copy_url_msg = self.driver.find_element_by_css_selector("div.popup div.popup-body div.button-div span.url-message").text
			self.assertEqual(copy_url_msg, "URL copied to clipboard!")
			
			self.driver.get(share_url) #open share url
			self.assertEqual(self.driver.current_url, share_url)			
		except Exception as e:
			self.driver.save_screenshot(os.getcwd() + os.path.sep + unittest.TestCase.id(self).split(".")[2] + ".png") 			
			self.fail(e)			



if __name__ == '__main__':    
	unittest.main()
