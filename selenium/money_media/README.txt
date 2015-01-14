I was not able to get my 2 test cases passing.
The reason for failure was inability to make login function work.  
login form appears to be nested within a hidden container, and so when attempting to interact with form elements I am getting ElementNotVisibleException.  Tried many different approaches using the ExpectedConditions class, however none works.  

I wanted to show the test passing so i have commented out login() call in testcase1 & 2...please uncomment to see failure

I have some post-login steps that should verify the scenarios. there is room to verify more content but I have not since there is no use right now.

also only tested on firefox not with chrome

to run it:
install python and selenium2 module
run the script from command line
> python money_media.py

