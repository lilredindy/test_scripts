#require "rubygems"
require "test/unit"
require "watir-webdriver"
 
class ShaveClubSocial < Test::Unit::TestCase

####################################################
  
 	def setup 
		@browser ||= Watir::Browser.new :firefox
  	end
   
  	def teardown 
    	@browser.close
  	end

#####################################################  


######################################################

    def test_sitemap_facebook
        @browser.goto "https://www.dollarshaveclub.com/"
        #@browser.wait_until {@browser.element(:xpath, "").exists?}
        #@browser.driver.manage.timeouts.implicit_wait = 10
        @browser.element(:xpath => "/html/body/div[1]/div[2]/div[1]/div[12]/ul/li[1]/a").click
        assert @browser.url == "https://www.facebook.com/DollarShaveClub"
    end

	def test_sitemap_twitter
        @browser.goto "https://www.dollarshaveclub.com/"
        @browser.element(:css => '#twitter > a').click
        assert @browser.url == "https://twitter.com/DollarShaveClub"
  	end

  	def test_sitemap_google
        @browser.goto "https://www.dollarshaveclub.com/"
        @browser.element(:id => 'google').click
	    assert @browser.url == "https://plus.google.com/+DollarShaveClub"
  	end


  	def test_sitemap_youtube
        @browser.goto "https://www.dollarshaveclub.com/"
        @browser.element(:id => 'youtube').click
        assert @browser.url == "https://www.youtube.com/user/DollarShaveClub"
  	end

  	def test_sitemap_pinterest
        @browser.goto "https://www.dollarshaveclub.com/"
        @browser.element(:id => 'pinterest').click
        assert @browser.url == "https://www.pinterest.com/dollarshaveclub"
  	end

  	def test_sitemap_instagram
        @browser.goto "https://www.dollarshaveclub.com/"
        @browser.element(:id => 'instagram').click
        assert @browser.url == "https://www.instagram.com/dollarshaveclub/"
  	end
end


