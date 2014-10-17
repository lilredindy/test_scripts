#test book
require_relative 'book'

describe Book do

	before :each do
		@book = Book.new "Cat's Cradle", "Kurt Vonnegut", :fiction
	end

	describe '#new' do 
		it "should take 3 params and returns a book" do
			@book.should be_an_instance_of Book
		end
	end 

	describe "#title" do
		it "should return the title" do
			@book.title.should eql "Cat's Cradle" 
		end
	end

	describe "#author" do
		it "should return the author" do
			@book.author.should eql "Kurt Vonnegut"
		end
	end

	describe "#category" do
		it "should return the category" do
			@book.category.should eql :fiction
		end
	end

end