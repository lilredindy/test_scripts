import os
import sys
import httplib
import base64
import json
import new
import unittest
import sauceclient
from selenium import webdriver
from sauceclient import SauceClient
import time

# it's best to remove the hardcoded defaults and always get these values
# from environment variables
USERNAME = os.environ.get('SAUCE_USERNAME', "shriamin")
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "abf4b3e5-cfab-4a79-824c-08a4d4d843f9")
sauce = SauceClient(USERNAME, ACCESS_KEY)
DEBUG  = 0

if DEBUG:
    browsers = [{"platform": "Mac OS X 10.9",
                 "browserName": "chrome",
                 "version": "31"},
                {"platform": "Windows 8.1",
                 "browserName": "internet explorer",
                 "version": "11"}]
else:
    browsers = [{'os': 'Windows', 'os_version': 'xp', 'browser': 'Firefox', 'browser_version': '35' },
                {'os': 'Windows', 'os_version': 'xp', 'browser': 'Firefox', 'browser_version': '35' },
                {"os":"ios","os_version":"7.0","browser":"iphone","device":"iPhone 5C"}]


def on_platforms(platforms):
    def decorator(base_class):
        #print base_class
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator


@on_platforms(browsers)
class SauceSampleTest(unittest.TestCase):
    def setUp(self):

        self.desired_capabilities['name'] = self.id()
        #print self.desired_capabilities['name']

        if DEBUG:
            sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
            self.driver = webdriver.Remote(
                desired_capabilities=self.desired_capabilities,
                command_executor=sauce_url % (USERNAME, ACCESS_KEY)
                )
            self.driver.implicitly_wait(30)

        else:
            bs_url = "http://shriamin1:LsuuTUS1h1RQ3aNGtZus@hub.browserstack.com:80/wd/hub"
            self.driver = webdriver.Remote(
                desired_capabilities=self.desired_capabilities,
                command_executor=bs_url
                )
            self.driver.implicitly_wait(30)

        print '\n' + self.driver.session_id


    def test_sauce(self):
        self.driver.get('http://saucelabs.com/test/guinea-pig')
        assert "I am a page title - Sauce Labs" in self.driver.title
        comments = self.driver.find_element_by_id('comments')
        comments.send_keys('Hello! I am some example comments.'
                           ' I should be in the page after submitting the form')
        self.driver.find_element_by_id('submit').click()

        commented = self.driver.find_element_by_id('your_comments')
        assert ('Your comments: Hello! I am some example comments.'
                ' I should be in the page after submitting the form'
                in commented.text)
        body = self.driver.find_element_by_xpath('//body')
        assert 'I am some other page content' not in body.text
        self.driver.find_elements_by_link_text('i am a link')[0].click()
        body = self.driver.find_element_by_xpath('//body')
        assert 'I am some other page content' in body.text

    def tearDown(self):

        if DEBUG:
            print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
            try:
                if sys.exc_info() == (None, None, None):
                    sauce.jobs.update_job(self.driver.session_id, passed=True)
                else:
                    sauce.jobs.update_job(self.driver.session_id, passed=False)
            finally:
                self.driver.quit()
        else:
            try:
                cmd = None
                if sys.exc_info() == (None, None, None):
                    cmd = "curl -ku \"shriamin1:LsuuTUS1h1RQ3aNGtZus\" -X PUT -H \"Content-Type: application/json\" -d \"{\\\"status\\\":\\\"completed\\\", \\\"reason\\\":\\\"cuz\\\"}\" https://www.browserstack.com/automate/sessions/%s.json"
                    print '\n' + cmd % self.driver.session_id
                    os.system(cmd % self.driver.session_id)
                else:
                    cmd = "curl -ku \"shriamin1:LsuuTUS1h1RQ3aNGtZus\" -X PUT -H \"Content-Type: application/json\" -d \"{\\\"status\\\":\\\"error\\\", \\\"reason\\\":\\\"cuz\\\"}\" https://www.browserstack.com/automate/sessions/%s.json"
                    os.system(cmd % self.driver.session_id)
            finally:
                self.driver.quit()
            
       
        

if __name__ == '__main__':
    unittest.main()