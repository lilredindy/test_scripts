Feature: As a user of Moat I would like to quickly search for Ads  from the main webpage and see the affected results


Scenario Outline: Generic Search
	Go to the search website
	Type the string <str> into the search field
	Click search
	Verify results
	
	Examples:
	|str |
	| Orbitz |
	| PETCO | #all-caps
	| NewYorker | #spaces removed
	| New York Times | #multi-word
	| Nytimes | # alternate text
	| Bob Dylan | #non-brand
	| College | #subject
	| http://www.artnet.com | #url 
	| #KLM | #hashtag
	| Robert Half Techology Inc. | #abbrev
	| Art & Design | #special-chars
	| Art && Design | #special-chars
	| Art | Design | #special-chars
	| 1=1 | #sql injection
	| " or ""=" | #sql injection


Scenario: Empty string 
	Go to the search website
	Type the empty_string into the search field
	Click search
	Verify no result


Scenario Outline: 404 Error page
	Go to the search website
	Type the <str> into the search field
	Click search
	Verify 404 page 

	Examples:
	|str |
	| **** |
	| ___ |
	

Scenario: Verify search bar attributes
	Go to the search website
	Verify existence of search bar
	Verify placehoder text in search bar
	Verify the text label for search bar
	Verify dimensions and placement of search bar


Scenario: Verify responsive design
	Go to the search website
	Increase the font size (Ctrl + '+')
	Verify existence of search bar
	Verify placehoder text in search bar
	Verify the text label for search bar
	Verify dimensions and placement of search bar


Scenario: Clear browsing data
	Clear browsing data in browser
	Go to the search website
	...


Scenario: Disable flash player
	Disable flash player plug-in
	Go to the search website
	...
	
Scenario: Disable java
	Disable java 
	Go to the search website
	...

Scenario: Verify auto-complete 
	Go to the search website
	Type the string <str> into the search field
	Verify down-down of matches



	




