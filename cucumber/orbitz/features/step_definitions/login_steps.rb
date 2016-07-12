require "watir-webdriver"
require "rspec/expectations"

Given /^on the sign-up page$/ do
	@browser.driver.manage.window.maximize
	@browser.goto "https://www.orbitz.com/user/createaccount"
end

When /^the completed registration form is submitted$/ do
	@browser.text_field(:id => "create-account-firstname").set "bob"
	@browser.text_field(:id => "create-account-lastname").set "cross"
	email_suffix = rand(36**5).to_s(36)
	@browser.text_field(:id => "create-account-emailId").set "bob.cross@#{email_suffix}.com"
	@browser.text_field(:id => "create-account-password").set "maverick"
	@browser.text_field(:id => "create-account-confirm-password").set "maverick"
	@browser.checkbox(:name => "marketing-email-opt-in").clear 
	#Element is not clickable at point SeleniumWebdriverException
	@browser.checkbox(:name => "create-account-expedia-policy").send_keys :space
	@browser.button(:id => "create-account-submit-button").click
end

When(/^the form is submitted with pre\-used e\-mail$/) do
    @browser.text_field(:id => "create-account-firstname").set "bob"
    @browser.text_field(:id => "create-account-lastname").set "cross"
	#since tests can be run in any order then no gaurantee e-mail exists
    @browser.text_field(:id => "create-account-emailId").set "bob.cross@gmail.com"
    @browser.text_field(:id => "create-account-password").set "maverick"
    @browser.text_field(:id => "create-account-confirm-password").set "maverick"
    @browser.checkbox(:name => "marketing-email-opt-in").clear
    #Element is not clickable at point SeleniumWebdriverException
    @browser.checkbox(:name => "create-account-expedia-policy").send_keys :space
    @browser.button(:id => "create-account-submit-button").click
end

Then /^an orbitz account is created$/ do
end

And /^i'm brought to flight search page$/ do
	@browser.screenshot.save 'screenshot.png'
	#expect(@browser.text).to include("Hello, bob")
    Watir::Wait.until { @browser.text.include? "Hello, bob" }
end 

Then(/^form displays account exists error$/) do
    Watir::Wait.until { @browser.text.include? "Account already exists" }
	#expect(@browser.text).to include("Account already exists.")
end

When(/^sign\-up via facebook is completed$/) do
	@browser.button(:id => "e3createaccont-facebook-button").click
	@browser.window(:title => "Facebook").use do
		@browser.text_field(:id => "email").set "foo"
		@browser.text_field(:id => "pass").set "bar"
	end 
end
