#require "rubygems"
require "test/unit"
require "watir-webdriver"
 
class GoogleSearch < Test::Unit::TestCase
  def setup 
    @browser ||= Watir::Browser.new :firefox
  end
   
  def teardown 
    @browser.close
  end
  
  def test_search
    @browser.goto "google.com"
    @browser.text_field(:name => "q").set "watir"
    @browser.button.click 
    @browser.div(:id => "resultStats").wait_until_present 
    assert @browser.title == "watir - Google Search"
  end


	#Given I am on the google search page
	#Then I should see the google logo
	def test_google_logo	
		@browser.element(:id => "foo").click
	end

end
