Feature:  As a user I want to be able to search the site so I can retrieve content quickly


Scenario Outline:  Word search
     Given I am on the main page   
     when I enter the search term "<text>" 
     and I click search button
     then I should see the search results

     Examples:
	| text |
    | capitalism |
    | two words |





