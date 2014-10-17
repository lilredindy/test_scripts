require '../Codebreaker/Game'


describe Codebreaker::Marker do
	describe '#exact_match_count' do		
		context "with no matches" do
			it "returns 0" do
				marker = Codebreaker::Marker.new('1234','5555')
				marker.exact_match_count.should ==0
			end
		end
		context "with 1 exact match" do
			it "returns 1" do
				marker = Codebreaker::Marker.new('1234','1555')
				marker.exact_match_count.should ==1
			end
		end
		context "with 1 number match" do
			it "returns 0" do
				marker = Codebreaker::Marker.new('1234','2555')
				marker.exact_match_count.should ==0
			end
		end
		context "with 1 exact match and 1 number match" do
			it "returns 1" do
				marker = Codebreaker::Marker.new('1234','1525')
				marker.exact_match_count.should ==1
			end
		end
	end
	describe '#number_match_count' do
		context "with no matches" do
			it "returns 0" do
				marker = Codebreaker::Marker.new('1234','5555')
				marker.number_match_count.should ==0
			end
		end
		context "with 1 number match" do
			it "returns 1" do
				marker = Codebreaker::Marker.new('1234','2555')
				marker.number_match_count.should ==1
			end
		end
		context "with 1 exact match" do
			it "returns 0" do
				marker = Codebreaker::Marker.new('1234','1555')
				marker.number_match_count.should ==0
			end
		end
		context "with 1 exact match and 1 number match" do
			it "returns 1" do
				marker = Codebreaker::Marker.new('1234','1355')
				marker.number_match_count.should ==1
			end
		end
		context "with 1 exact match duplicated in guess" do
			it "returns 0" do
				marker = Codebreaker::Marker.new('1234','1155')
				marker.number_match_count.should ==0
			end
		end
	end
end


describe Codebreaker::Game do
	before :each do
		@output = double('output').as_null_object
		@game = Codebreaker::Game.new(@output)
	end
	describe '#start' do
		it 'send a welcome message' do
			@output.should_receive(:puts).with('Welcome to Codebreaker!')
			@game.start('1234')
		end
		it 'prompts for first guess' do 
			@output.should_receive(:puts).with('Enter guess:')
			@game.start('1234')
		end
	end
	describe "#guess" do
		context "with no matches" do
			it "sends a mark with ''" do
				@game.start('1234')
				@output.should_receive(:puts).with('')
				@game.guess('5555')
			end
		end
		context "with 1 number match" do
			it "sends a mark with '-'" do
				@game.start('1234')
				@output.should_receive(:puts).with('-')
				@game.guess('2555')
			end
		end
		context "with 1 exact match" do
			it "sends a mark with '+'" do
				@game.start('1234')
				@output.should_receive(:puts).with('+')
				@game.guess('1555')
			end
		end
		context "with 2 number matches" do
			it "sends a mark with '--'" do
				@game.start('1234')
				@output.should_receive(:puts).with('--')
				@game.guess('2355')
			end
		end
		context "with 3 exact matches" do
			it "sends a mark with '+++'" do
				@game.start('1234')
				@output.should_receive(:puts).with('+++')
				@game.guess('1254')
			end
		end
		context "with 1 number match and 1 exact match (in that order)" do
			it "sends a mark with '+-'" do
				@game.start('1234')
				@output.should_receive(:puts).with('+-')
				@game.guess('2535')
			end
		end
	end
end
