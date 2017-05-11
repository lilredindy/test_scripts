Feature: As A user I want to obtain detailed information about a specific ad (legacy, publisher(s), creator, dates, dimensions


Scenario: Verify results page thumbnails
	Go to the search website
	Type the string "Moat" into the search field
	Click search
	Mouse-over ad impression on result page
	Verify the contents of popup
