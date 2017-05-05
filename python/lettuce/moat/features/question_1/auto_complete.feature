Feature: As a user I want to see a list of choices that are related to my search criteria


Scenario: Search for "New Yorker"
    Go to the search website
    Type first word "New" into search bar
    See related items in the dropdown list within the search bar
	Finish the string and type search
    Now I am re-directed to the results page


Scenario: Search for "Alex Katz"  
	Go to the search website
	Type "Alex Katz" into search bar
	Click search
	See the result as "Katzkin"
	
