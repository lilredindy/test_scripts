require 'selenium-webdriver'


driver = Selenium::WebDriver.for :firefox


Before do |scenario|
	@driver = driver
end


