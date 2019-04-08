import unittest
import logging
import sys
import inspect

#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains


from appium import webdriver
import time

from subprocess import call


global logger
logger = logging.getLogger(__name__) #__name__ == __main__
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


    ##################################
    # SETUP AND TEARDOWN 
    ##################################

class MobileSafariTests(unittest.TestCase):

  def setUp(self):
    logger.debug(inspect.stack()[0][3])

    desired_caps = {
      'platformName': 'iOS',
      'deviceName': 'iPhone sucks (10.3.3)',
      'platformVersion':'',
      #'udid': '4443449a13de797bc614c5d0fe785168371a7492',
      'automationName': 'XCUITest',
      #'bundleId': 'com.apple.Preferences',
      'browserName': 'Safari',
      "startIWDP": True,
	    "udid": "auto",
      #'usePrebuiltWDA': True
    }
    self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
    #self.driver.implicitly_wait(5000) #THIS ACTUALLY WORKS WHEN SWTICHING APPS!!
    #self.driver.reset() #this seems to kill the app nothing more


  def tearDown(self):
      logger.debug(inspect.stack()[0][3])
      #self.driver.quit()




  ##################################
  # A BATTERY OF TESTS 
  ##################################

  #@unittest.skip("")
  def test1(self):
    logger.debug(inspect.stack()[0][3])
    #save some browser data and check persistence...
   # self.driver.get("http://www.gmail.com")
    #self.driver.delete_all_cookies() #doesn't work



if __name__ == '__main__':
    unittest.main()


