Feature:  Roundtrip Flight Search


Background:
Given the app is running

Scenario: Book a roundtrip flight without hotel
Given roundtrip flight form is showing
When flight itinerary is submitted
Then he recieves list of available flights

