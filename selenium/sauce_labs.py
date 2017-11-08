from selenium import webdriver

#sauce_url = "http://shriamin:abf4b3e5-cfab-4a79-824c-08a4d4d843f9@ondemand.saucelabs.com:80/wd/hub"
sauce_url = "http://lilredindy:6cd6bec2-262a-40e6-8097-2cb684c3f8b6@ondemand.saucelabs.com:80/wd/hub"

desired_capabilities = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}

driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=sauce_url)
driver.implicitly_wait(5)

driver.get('http://google.com')
assert "Google" in driver.title
driver.quit()