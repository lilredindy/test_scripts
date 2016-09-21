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
<<<<<<< HEAD
		headline = article.a(:class => "article-link").h1(:class => "hed").text
		puts headline
=======
		heading_text = article.a(:class => "article-link").h1(:class => "hed").text
		puts heading_text
>>>>>>> e14b33e123ad90c675876fb60e7a955320a2e854
		
		assert @browser.windows.size == 1
		article.click(:shift) #this opens article in a new window
		# Watir::Wait.until { browser.windows.size == 2 }
		assert @browser.windows.size == 2

<<<<<<< HEAD
		assert @browser.text.include? headline
		
		@browser.window(index: 1).close	#closes active (top) window
=======
		assert @browser.text.include? heading_text
		
		@browser.window(index: 1).close	
>>>>>>> e14b33e123ad90c675876fb60e7a955320a2e854
	end    
  end


end
