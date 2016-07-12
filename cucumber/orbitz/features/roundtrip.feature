Feature:  Roundtrip Flight Search


Scenario: Book a roundtrip flight without hotel
Given roundtrip-flight form is presented
When the completed roundtrip-flight form is submitted
Then I should see available flights


Scenario:  blank return date
Given roundtrip-flight form is presented
When the form is filled but the return date is left blank 
Then the return date field is auto-filled

