
Feature:  As a user of indeed I want to login so that I can search for a job


@deprecated
Scenario: Valid credentials
     Given I am on the login screen  
     when I enter a valid username
     and I enter a valid password 
     and I click submit
     then I should be logged in 
     and I should see my account settings


@wip
Scenario: Valid credentials
     Given I am on the login screen  
     when I submit valid credentials
     then I should be logged in 
     and I should see my account settings



@deprecated
Scenario Outline: Invalid credentials
     Given I am on the login screen  
     when I enter the invalid credentials "<username>" and "<password>"
     and I click submit
     then I should see bad credentials error message

     Examples:
	| username | password |
    | foo@gmail.com | foo | 
    | shri.amin@gmail.com | mav |
    | shri.amin | maverick|
    | maverick	| shri.amin@gmail.com |


Scenario Outline: Invalid credentials
     Given I am on the login screen  
     when I submit invalid credentials "<username>" and "<password>"
     then I should see bad credentials error message

     Examples:
	| username | password |
    | foo@gmail.com | foo | 
    | shri.amin@gmail.com | mav |
    | shri.amin | maverick|
    | maverick	| shri.amin@gmail.com |

@wip
Scenario:  Login link unecessary
	Given I am on the login screen
	Then I should not see a sign in link


Scenario:  Already logged in
	Given I am already logged in
	When I attempt to access login page
	Then I should be redirected to my account page

@deprecated
Scenario:  three invalid password attempts
    Given I am on the login screen  
    when I enter a valid username
    and I submit an invalid password three times
    	|bad_pwd |
    	|badpwd1_dafdf|
    	|badpwd2_fjyfhj|
    	|badpwd3_erer|
	Then I should see retry in five minutes error message


Scenario: three invalid password attempts
     Given I am on the login screen  
     when I submit valid email with invalid password three times
        |bad_pwd |
    	|badpwd1_dafdf|
    	|badpwd2_fjyfhj|
    	|badpwd3_erer|
     then I should see retry in five minutes error message


Scenario: default state for login page
	Given I am on the login screen
	then the username and password fields should be blank
