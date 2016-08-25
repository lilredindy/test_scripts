#require "rubygems"
require "test/unit"
require "watir-webdriver"
 
class Atlantic  < Test::Unit::TestCase
  def setup 
    @browser ||= Watir::Browser.new :firefox
	@browser.driver.manage.window.maximize
  end
   
  def teardown 
    @browser.close
  end
  
  def test_articles
    @browser.goto "theatlantic.com"

	#this only gets the first set of articles
    articles = @browser.ul(:class => "articles").lis(:class => "article")
	
	articles.each do |article|
		puts article.a(:class => "article-link").attribute_value("href")
		heading_text = article.a(:class => "article-link").h1(:class => "hed").text
		puts heading_text
		
		assert @browser.windows.size == 1
		article.click(:shift) #this opens article in a new window
		# Watir::Wait.until { browser.windows.size == 2 }
		assert @browser.windows.size == 2

		assert @browser.text.include? heading_text
		
		@browser.window(index: 1).close	
	end    
  end


end
