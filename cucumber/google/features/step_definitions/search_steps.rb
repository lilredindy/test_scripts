require "watir-webdriver"
require "rspec/expectations"
 
#Note: the browser open and close call is in env.rb

Given /^I have entered "([^"]*)" into the query$/ do |term|
  #@browser ||= Watir::Browser.new :firefox
  @browser.goto "google.com"
  @browser.text_field(:name => "q").set term
end
 
When /^I click "([^"]*)"$/ do |button_name|
  @browser.button.click
end
 
Then /^I should see some results$/ do
  @browser.div(:id => "resultStats").wait_until_present
  expect(@browser.div(:id => "resultStats")).to exist
  #@browser.close
end


Given(/^I am on the search page$/) do
    @browser.goto "google.com"
end

Then(/^I should see the google logo$/) do
	expect(@browser.element(:id => "hplogo")).to exist
end
