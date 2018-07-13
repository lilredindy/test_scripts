import unittest
import sys

#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium import webdriver
import time

from subprocess import call


class appium_foodmento(unittest.TestCase):

    def setUp(self):
      print ("setup")
      desired_caps = {
        'platformName': 'iOS',
        'deviceName': 'iPhone sucks (10.3.3)',
        'platformVersion':'',
        'udid': '4443449a13de797bc614c5d0fe785168371a7492',
        'automationName': 'XCUITest',
        'bundleId': 'com.foodmento.foodmento',
        #'usePrebuiltWDA': True
      }
      self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)


    def test_simple_example1(self):
        print ("test")
        # Test Actions Here

        self.driver.find_element_by_accessibility_id('Discover all').click()
       # time.sleep(10)
        #self.driver.find_element_by_accessibility_id('Pause').click()
        

    #def test_simple_example2(self):
     #   print ("test2")
        # Test Actions Here

        
        #self.driver.find_element_by_accessibility_id('Discover All').click()
       # time.sleep(10)
        #self.driver.find_element_by_accessibility_id('Pause').click()
        


    def tearDown(self):
        print ("teardown")
        self.driver.quit()
      

if __name__ == '__main__':
    unittest.main()