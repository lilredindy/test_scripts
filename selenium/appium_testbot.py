import unittest
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from testingbotclient import TestingBotClient

class TestTestingBotClient(unittest.TestCase):

    def setUp(self):
        desired_cap = {
      'app': 'http://appium.s3.amazonaws.com/WebViewApp7.1.app.zip',
      'version': '11.2',
      'platform': 'iOS',
      'deviceName': 'iPhone X',
      'platformName': 'iOS',
      'name' : 'My First Mobile Test',
        }

        self.driver = webdriver.Remote(
            command_executor='https://e9119262abca817b6e89829a3f3b39ed:10b7b3f28b761a8190a08d262506b227@hub.testingbot.com/wd/hub',
            desired_capabilities=desired_cap)

    def test_simple_example(self):
        # Test Actions Here
        pass

    def tearDown(self):
        self.driver.quit()
        status = sys.exc_info() == (None, None, None)
        tb_client = TestingBotClient('e9119262abca817b6e89829a3f3b39ed', '10b7b3f28b761a8190a08d262506b227')
        tb_client.tests.update_test(self.driver.session_id, self._testMethodName, status)

if __name__ == '__main__':
    unittest.main()