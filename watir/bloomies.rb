#require "rubygems"
require "test/unit"
require "watir-webdriver"
#require "testrail_client"
require "./testrail.rb"
 
class Bloomies < Test::Unit::TestCase

####################################################

	def setup 
		@browser ||= Watir::Browser.new :firefox
	end
   
	def teardown 
		@browser.close
	end

#####################################################  


######################################################


    def test_open_base_url
        @browser.goto "http://www.bloomingdalesjobs.com/"
        #@browser.wait_until {@browser.element(:xpath, "").exists?}
        #@browser.driver.manage.timeouts.implicit_wait = 10
        assert @browser.url == "http://www.bloomingdalesjobs.com/"
    end

end
