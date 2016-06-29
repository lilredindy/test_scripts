require 'selenium-webdriver'


Given /^the app is running$/ do
	@driver.navigate.to "http://www.orbitz.com"
end 


Given /^roundtrip flight form is showing$/ do
	element1 = @driver.find_element(:id, 'tab-flight-tab')
	element1.click()
	element2 = @driver.find_element(:id, 'flight-type-roundtrip-label')
	element2.click()
end



When /^flight itinerary is submitted?/ do 
	origin = @driver.find_element(:id, 'flight-origin')
	origin.send_keys "New York"
	dest = @driver.find_element(:id, 'flight-destination')
	dest.send_keys "Se"
	list_item = @driver.find_element(:css, '#aria-option-0')
	list_item.click()
	depart_date = @driver.find_element(:id, 'flight-departing')
	depart_date.send_keys ('07/09/2016')
	return_date = @driver.find_element(:id, 'flight-returning')
	return_date.send_keys ('07/23/2016')
	search = @driver.find_element(:id, 'search-button')
	search.click()
end
