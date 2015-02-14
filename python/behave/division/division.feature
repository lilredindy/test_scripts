Feature: As a math guy I want to be able do a division of two numbers and get the result


Scenario Outline: Divide two positive integers
     Given we have two positive integers "<a>" and "<b>" 
     when we divide "<a>" by "<b>"
     then the result "<c>" will be positive

Examples:
	| a | b | c |
    | 35 | 5 | 7|
    | 34 | 2 | 17 |
	| 16 | 2 | 9 |


