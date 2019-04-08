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


class IOSSettingsTests(unittest.TestCase):
  ##################################
  # SETUP AND TEARDOWN 
  ##################################

  def setUp(self):
          
    desired_caps = {
      'platformName': 'iOS',
      'deviceName': 'iPhone sucks (10.3.3)',
      'platformVersion':'',
      'udid': '4443449a13de797bc614c5d0fe785168371a7492',
      'automationName': 'XCUITest',
      'bundleId': 'com.apple.Preferences',
    }

    self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    #self.driver.implicitly_wait(5000) #THIS ACTUALLY WORKS WHEN SWTICHING APPS!!



  def tearDown(self):
      #FoodmentoActions.logout(self.driver) #
      logger.debug(inspect.stack()[0][3])
      #self.driver.quit()




  ##################################
  # A BATTERY OF TESTS 
  ##################################
  
  #@unittest.skip("")
  def test_deleteSafariUserData(self):

      logger.debug(inspect.stack()[0][3])

      #self.driver.execute_script('mobile: activateApp', {'bundleId': 'com.apple.Preferences'})
      
      #self.driver.execute_script('mobile: scroll', {'': ''});

      

      #ACTIONCHAINS (AKA MOUSE) IS NOT AVAILABLE FOR IOS, USE TOUCH ACTIONS INSTEAD
     # actions = ActionChains(self.driver)
      #actions.move_to_element(element)
      #actions.click(element)
      #actions.perform()

      #WHATS THE DIFF BTWN EXECUTE_MOBILE_CMDS AND TOUCH ACTIONS??
      #THIS TEST TAKES LONG TIME...TOO LONG...LIKE 3 MINUTES 
      self.driver.execute_script('mobile:scroll',{'name':"Safari" } ) #APPIUM BUG, LIMITED SCROLLING...
      self.driver.execute_script('mobile:scroll',{'name':"Safari" } ) #...NEEDS TO BE CALLED TWICE
      element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Safari")))
      self.driver.execute_script('mobile: tap', {'element': element, 'x': 0 , 'y': 0  }) #(0,0) works
      self.driver.execute_script('mobile:scroll',{'name':"Clear History and Website Data" } ) #...NEEDS TO BE CALLED TWICE
      self.driver.execute_script('mobile:scroll',{'name':"Clear History and Website Data" } ) #...NEEDS TO BE CALLED TWICE
      element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Clear History and Website Data")))
      self.driver.execute_script('mobile: tap', {'element': element, 'x': 0 , 'y': 0  }) #(0,0) works
      element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Clear History and Data")))
      self.driver.execute_script('mobile: tap', {'element': element, 'x': 0 , 'y': 0  }) #(0,0) works  
      #actions = TouchAction(self.driver)
      #actions.tap(element) 
      #actions.perform()


if __name__ == '__main__':
    unittest.main()


