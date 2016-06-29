require 'selenium-webdriver'

#profile = Selenium::WebDriver::Firefox::Profile.new
#profile['browser.startup.homepage'] = 'about:blank'
#profile['startup.homepage_welcome_url'] = 'about:blank'
#profile['startup.homepage_welcome_url.additional'] = 'about:blank'
#profile['browser.startup.homepage_override.mstone'] = 'ignore'
#profile['startup.homepage_welcome_url.additional'] = 'about:blank'
#driver = Selenium::WebDriver.for :firefox, :profile => profile

driver = Selenium::WebDriver.for :firefox


#driver.get 'http://www.orbitz.com'
driver.navigate.to "http://www.orbitz.com"
origin = driver.find_element(:id, 'package-origin')
origin.send_keys "New York"

dest = driver.find_element(:id, 'package-destination')
dest.send_keys "Se"
list_item = driver.find_element(:css, '#aria-option-0')
list_item.click()

#element.submit
#puts driver.title
#driver.quit

#driver.close


