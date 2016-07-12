require "watir-webdriver"
#require "rspec/expectations"

Given /^roundtrip-flight form is presented$/ do
	@browser.goto "orbitz.com"
    @browser.element(:id => "tab-flight-tab").click
    @browser.element(:id => "flight-type-roundtrip-label").click
end

When /^the completed roundtrip-flight form is submitted$/ do 
	@browser.text_field(:id => 'flight-origin').set 'New York'
    @browser.text_field(:id => 'flight-destination').set 'Seattle'
    @browser.text_field(:id => 'flight-departing').set '7/11/2016'
    @browser.text_field(:id => 'flight-returning').set '7/21/2016'
    @browser.button(:id => 'search-button').click
end

Then(/^I should see available flights$/) do
	Watir::Wait.until { @browser.text.include? "Select your roundtrip flight to Seattle" }
	#expect(@browser.text).to include("Select your roundtrip flight to Seattle") 
end


When(/^the form is filled but the return date is left blank$/) do
    @browser.text_field(:id => 'flight-origin').set 'New York'
    @browser.text_field(:id => 'flight-destination').set 'Seattle'
    @browser.text_field(:id => 'flight-departing').set '7/11/2016'
    @browser.text_field(:id => 'flight-returning').set ''
    @browser.text_field(:id => 'flight-returning').send_keys :tab
end

Then(/^the return date field is auto\-filled$/) do
    expect(@browser.text_field(:id => 'flight-returning').value).to eq('07/11/2016')
end

