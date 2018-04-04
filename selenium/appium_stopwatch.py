import unittest
import sys

#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from testingbotclient import TestingBotClient
from appium import webdriver
import time


class StopWatchTests(unittest.TestCase):

    def setUp(self):
      desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '9.3',
        'deviceName': 'iPhone Simulator',
        'automationName': 'XCUITest',
        'app': '/Users/shriamin/Library/Developer/Xcode/DerivedData/Stop_Watch-bwidymufpkrbuqfpyzosxoqyjqip/Build/Products/Debug-iphonesimulator/StopWatch.app',
      }
      self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    def test_simple_example(self):
        # Test Actions Here
        self.driver.find_element_by_accessibility_id('Start').click()
        time.sleep(10)
        self.driver.find_element_by_accessibility_id('Pause').click()
        


    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()