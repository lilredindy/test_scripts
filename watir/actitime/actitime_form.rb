#require "rubygems"
require "test/unit"
require "watir-webdriver"
 
class ActiTimeForm < Test::Unit::TestCase

####################################################
  
	def setup 
		@browser ||= Watir::Browser.new :firefox
		@browser.driver.manage.window.maximize
	end

	def teardown 
        @browser.close
	end

#####################################################  


######################################################
=begin
    def test_url
        @browser.goto "https://www.actitime.com/free-online-trial.php"
        #@browser.wait_until {@browser.element(:xpath, "").exists?}
        #@browser.driver.manage.timeouts.implicit_wait = 10
        assert @browser.url == "https://www.actitime.com/free-online-trial.php"
    end


	def test_all_blank_form
		@browser.goto "https://www.actitime.com/free-online-trial.php"
		@browser.button(:name => "sendRequest").click
		assert @browser.alert.exists?
		assert_match  "First", @browser.alert.text
		assert_match  "Last", @browser.alert.text
		assert_match  "Email", @browser.alert.text
		@browser.alert.ok
	end


	#Given I enter all valid form field values 
	#When the email field value is blank
	#And I submit the form
	#Then I should see an alert with email error
	def test_blank_email_only
		@browser.goto "https://www.actitime.com/free-online-trial.php"
        @browser.text_field(:name => "firstName").send_keys "shri"
        @browser.text_field(:name => "lastName").send_keys "amin"
		@browser.button(:name => "sendRequest").click
		assert @browser.alert.exists?
        assert_no_match  /First/, @browser.alert.text
	    assert_no_match  /Last/, @browser.alert.text
        assert_match  /Email/, @browser.alert.text
        @browser.alert.ok
	end
=end

	def test_for_reused_email
		@browser.goto "https://www.actitime.com/free-online-trial.php"
        @browser.text_field(:name => "firstName").send_keys "shri"
        @browser.text_field(:name => "lastName").send_keys "amin"
        @browser.text_field(:name => "emailAddress").send_keys "lilredindy@gmail.com"
		@browser.button(:name => "sendRequest").click
		assert @browser.url == "https://www.actitime.com/free-online-trial.php#"
		err_txt = "The specified e-mail address has already been used to request a trial account. You cannot request multiple trial accounts using the same e-mail address."
		assert @browser.element(:text, err_txt).present?
		assert @browser.text_field(:name => "firstName").value == "shri"
	end


	
end
