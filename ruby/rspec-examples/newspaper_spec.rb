
class Newspaper
	def colors
		colors = ['black', 'white']
	end
end

describe Newspaper do
	it "should be black" do
		expect(Newspaper.new.colors).to include('black')
	end
	it "should be white" do
		expect(Newspaper.new.colors).to include('white')
	end
	it "should have 2 colors" do
		expect(Newspaper.new.colors.count).to eql(3)
	end

end
