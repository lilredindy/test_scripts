
Feature: Search In order to use Google users must be able to search for content 


Scenario: Search for a term
    Given I have entered "watir" into the query
    When I click "search"
    Then I should see some results


Scenario: Check for logo
	Given I am on the search page
	Then I should see the google logo

Scenario:  Unimplemented Scenario
	Given I have A
	When I do B
	Then I should get C


