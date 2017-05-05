Feature: As a user I want to search for ads from the main page


Scenario Outline: Generic Search
	Go to the search website
	verify existence of search bar
	verify placehoder text
	verify existence of search icon
	verify existence of searchbar label
	verify searchbar exists within the html tag <div id="grey-blob">
	Type the string <str> into the search field
	Click search
	Now I am re-directed to the results page
    And I should see a text label for the search query on results page
    And I should be presented with thumbnails for ads on result page
    And the ads should be displayed in table format
	And the ads should be relavant to the search
    And there should be search bar on the top of the page for my next search
	And results page should be presented and fully loaded in one second
	 
	
	Examples:
	|str |
	| Bob Dylan |
	| Dylan |
	| Dylan,Bob |
	| Bob_Dylan |
	| #BobDylan|
	| Petco |
	| PETCO |
	| New York Times |
	| nytimes.com |
	| http://www.artnet.com |
	| Robert Half Technology Inc. |
	| Robert Zimmerman? |
	| Art & Music |
	|  | #empty string


Scenario:  Check responsive design for search page
	Go to the search website
	Increase the display size for text of the browser
	Verify the search bar is visible 
    Type the string into the search field
    Click search
    Now I am re-directed to the results page


Scenario: pre-defined searches
	Go to the search website
	click a link from set of pre-defined examples
	Now I am re-directed to the results page
	And the ads should be relavant to the search


Scenario: remove browsing history or cache
Scenario: Disable flash player, java, etc







	




