
class Newspaper
	def colors
		colors = ['black', 'white']
	end
end

describe Newspaper do
	it "should be black" do
		Newspaper.new.colors.should include('black')
	end
	it "should be white" do
		Newspaper.new.colors.should include('white')
	end
	it "should have 2 colors" do
		Newspaper.new.colors.count.should eql(3)
	end
	it "should be read all over"
end
