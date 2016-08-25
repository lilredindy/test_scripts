
Feature: As I tester of NBA.com, I want to ensure things work 


Scenario Outline: sitemap links
  Given I am on the nba home page
  And sitemap link title "<link_title>" is present
  When I click on the sitemap link titled "<link_title>"
  Then I should arrive at correct "<dest_url>"

  Examples: 
    | link_title | dest_url |
    | About the NBA | http://www.nba.com/news/about/index.html?ls=iref:nba:gfooter |     
#    | Contact Us | http://contact.nba.com/ |    
#    | Career Opportunities | http://careers.nba.com/ |    
#    | Closed Captioning | http://www.nba.com/news/closed_captioning.html?ls=iref:nba:gfooter |     
#	| Important Dates | http://www.nba.com/news/important-dates/index.html?ls=iref:nba:gfooter |
#	| FAQs |http://www.nba.com/news/faq/index.html?ls=iref:nba:gfooter |


Scenario: Verify big content appears
	Given I am on the nba home page
	Then I should see six big blocks of content


