from selenium import webdriver

sauce_url = "http://blueguyredgirl:50daa0e9-b0c7-46fc-b553-b56863711a35@ondemand.saucelabs.com:80/wd/hub"

desired_capabilities = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "55",
}

driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=sauce_url)
driver.implicitly_wait(5)

driver.get('http://google.com')
assert "Google" in driver.title
driver.quit()