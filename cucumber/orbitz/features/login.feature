Feature: create an account

Scenario:
Given on the sign-up page
When the completed registration form is submitted
#Then an orbitz account is created
And i'm brought to flight search page


Scenario:
Given on the sign-up page
When the form is submitted with pre-used e-mail
Then form displays account exists error


Scenario:
Given on the sign-up page
When sign-up via facebook is completed
#Then an orbitz account is created 
#And i'm brought to flight search page

