Feature: create an account

Background:

Scenario: 
Given I want to sign up via e-mail
When I correctly submit the sign up form 
Then a new orbitz account is created 

Scenario:
Given I want to sign up via e-mail
When I incorrectly submit the sign up form
Then I recieve errors 

Scenario:
Given a new visitor wants to create an account
When he chooses to sign up via Facebook
Then a new orbitz account is created 



