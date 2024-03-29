from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'os': 'Windows', 'os_version': 'xp', 'browser': 'IE', 'browser_version': '7.0' }

driver = webdriver.Remote(
    command_executor='http://shriamin1:LsuuTUS1h1RQ3aNGtZus@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowerStack")
elem.submit()
print driver.title
assert (driver.title == "BrowerStack - Google Search")
driver.quit()
