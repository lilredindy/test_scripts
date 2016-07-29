#require "rubygems"
require "test/unit"
require "watir-webdriver"
 
class ShaveClubSitemap < Test::Unit::TestCase

####################################################
  
 	def setup 
		@browser ||= Watir::Browser.new :firefox
  	end
   
  	def teardown 
    	@browser.close
  	end

#####################################################  


######################################################

    def test_footer_shave
        @browser.goto "https://www.dollarshaveclub.com/"
        #@browser.wait_until {@browser.element(:xpath, "").exists?}
        #@browser.driver.manage.timeouts.implicit_wait = 10
        @browser.link(:text => "SHAVE").click
        assert @browser.url == "https://www.dollarshaveclub.com/our-products/shave"
    end

    def test_footer_style
        @browser.goto "https://www.dollarshaveclub.com/"
        @browser.link(:text => "STYLE").click
        assert @browser.url == "https://www.dollarshaveclub.com/our-products/style"
	end

    def test_footer_fresh   
        @browser.goto "https://www.dollarshaveclub.com/"
		@browser.link(:text => "FRESH").click
        assert @browser.url == "https://www.dollarshaveclub.com/our-products/fresh"
	end

    def test_footer_protect   
        @browser.goto "https://www.dollarshaveclub.com/"
        @browser.link(:text => "PROTECT").click
        assert @browser.url == "https://www.dollarshaveclub.com/our-products/protect"
    end


end
