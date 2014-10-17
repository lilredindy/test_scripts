require '../Codebreaker/Game'


class Output
	def messages
		@messages ||= []
	end

	def puts(message)
		messages << message
	end	
end

def output
	@output ||= Output.new
end

#feature: starts a game
When(/^I start a new game$/) do
	Codebreaker::Game.new(output).start
end

#Then and And are treated the same
Then(/^I should see "(.*?)"$/) do |message| 
	output.messages.should include(message)
end

#feature: submits a guess
Given(/^the secret code is "(.*?)"$/) do |secret|
	@game = Codebreaker::Game.new(output)
	@game.start(secret)
end

When(/^I guess "(.*?)"$/) do |guess|
	@game.guess(guess)
end

Then(/^the mark should be "(.*?)"$/) do |mark|
	output.messages.should include(mark)
end