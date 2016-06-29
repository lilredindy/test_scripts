require 'selenium-webdriver'

#caps = Selenium::WebDriver::Remote::Capabilities.firefox
#caps.version = "8"
#caps.platform = :WINDOWS

driver = Selenium::WebDriver.for(
  :firefox)
driver.navigate.to "http://www.google.com"
#element = driver.find_element(:name, 'q')
#element.send_keys "Hello WebDriver!"
#element.submit
puts driver.title
#driver.quit
