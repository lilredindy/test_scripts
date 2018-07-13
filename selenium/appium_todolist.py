import unittest
import sys

#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from testingbotclient import TestingBotClient
from appium import webdriver


class ToDoListsTests(unittest.TestCase):

    def setUp(self):
      desired_caps = {
        'platformName': 'iOS',
        #'platformVersion': '10.3',
        'deviceName': 'iPhone sucks',
        'udid': '4443449a13de797bc614c5d0fe785168371a7492',
        'automationName': 'XCUITest',
        #'app': '/Users/shriamin/Library/Developer/Xcode/DerivedData/todolist-dbyycwgvumhydzfgqtlgfohtsljz/Build/Products/Debug-iphonesimulator/todolist.app',
        'app': '/Users/shriamin/Library/Developer/Xcode/DerivedData/todolist-dbyycwgvumhydzfgqtlgfohtsljz/Build/Products/Debug-iphoneos/todolist.app',
      }
      
      self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
      self.driver.implicitly_wait(5)


    def test_simple_example(self):
        # Test Actions Here
        self.driver.find_element_by_accessibility_id('ADD NEW').click()
        self.driver.find_element_by_accessibility_id('task name').send_keys("eat")
        self.driver.find_element_by_accessibility_id('description').send_keys("gujarati food works")
        self.driver.find_element_by_accessibility_id('ADD TASK, button').click()
        self.driver.find_element_by_accessibility_id('TASKS').click()
        

    def tearDown(self):
        #self.driver.quit()
        pass

if __name__ == '__main__':
    unittest.main()