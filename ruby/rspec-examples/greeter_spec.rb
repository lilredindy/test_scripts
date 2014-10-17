#---
# Excerpted from "The RSpec Book",
# published by The Pragmatic Bookshelf.
# Copyrights apply to this code. It may not be used to create training material, 
# courses, books, articles, and the like. Contact us if you are in doubt.
# We make no guarantees that this code is fit for any purpose. 
# Visit http://www.pragmaticprogrammer.com/titles/achbd for more book information.
#---
describe "RSpec Greeter" do                                              
  it "should say 'Hello RSpec!' when it receives the greet() message" do 
    greeter = RSpecGreeter.new               
    greeter.greet.should == "Hello RSpec!" 
  end
end


class RSpecGreeter 
	def greet
		"Hello RSpec!"
	end
end
