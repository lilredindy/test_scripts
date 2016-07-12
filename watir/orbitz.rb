#require "rubygems"
require "test/unit"
require "watir-webdriver"
 
class OrbitzFlight < Test::Unit::TestCase
  def setup 
	@browser ||= Watir::Browser.new :firefox
  end
   
  def teardown 
    	@browser.close
  end
  
  def test_roundtrip
    	@browser.goto "orbitz.com"
    	@browser.element(:id => "tab-flight-tab").click
    	@browser.element(:id => "flight-type-roundtrip-label").click
	@browser.text_field(:id => 'flight-origin').set 'New York'
	@browser.text_field(:id => 'flight-destination').set 'Seattle'
	@browser.text_field(:id => 'flight-departing').set '7/11/2016'
        @browser.text_field(:id => 'flight-returning').set '7/21/2016'
	@browser.button(:id => 'search-button').click
		
  end
end
