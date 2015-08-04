import unittest
from selenium import webdriver


class HellTestCase(unittest.TestCase):

	def setUp(self):
		chrome_path = "C:\\Documents and Settings\\chuck\\Desktop\\shri\\Development\\test_tools\\selenium\\chromedriver.exe";
		#chrome_options = webdriver.ChromeOptions()
		#chrome_options.add_argument('--chrome_path=%s' % chrome_path)
		#System.setProperty("webdriver.chrome.driver", chrome_path);
		self.driver = webdriver.Chrome(executable_path=chrome_path)

	def test_get_page(self):
		self.driver.get('http://www.av1611.org/hell.html')
		try:
			text_element = self.driver.find_element_by_link_text("HELL IS A PLACE OF FIRE")
		except:
			print "No non-anchor element found!"
		try:
			text_element = self.driver.find_element_by_link_text("To order printed tracts.")
		except:
			print "No anchor element found!"
		try:
			text_element = self.driver.find_element_by_partial_link_text("To order")
		except:
			print "No partial link text found"
		try:
			text_element = self.driver.find_element_by_xpath("/html//tr[contains(.,'HELL')]")
		except:
			print "No XPATH ELEMENT found"

	def tearDown(self):
		self.driver.quit() 

if __name__ == '__main__':
	unittest.main()
