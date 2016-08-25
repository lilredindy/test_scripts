#require "rubygems"
require "test/unit"
require "watir-webdriver"
 
class NYTimes < Test::Unit::TestCase
	def setup 
    	@browser ||= Watir::Browser.new :firefox
		@browser.driver.manage.window.maximize
 		@browser.driver.manage.timeouts.implicit_wait = 25
  	end
   
  	def teardown 
    	@browser.close
  	end



	#Given a page with headlines
	#When I click on a headline
	#Then the user lands on the article page   

  	def test_click_headlines
    	@browser.goto "http://www.nytimes.com/column/state-of-the-art"

=begin
		h2s = @browser.h2s :class => "headline"
		assert h2s.length > 0
		headlines = Array.new
		h2s.each do |h2|
			headlines << h2.text
			#assert @browser.text.include? headline
			#@browser.back
		end

=end

		links = @browser.links :class => "story-link"
		assert links.length > 0
		
		links.each_with_index do |link,index|
  			puts links[index].text
  			links[index].click
  			@browser.back
  			links = @browser.links :class => "story-link"
		end	


	end
end
