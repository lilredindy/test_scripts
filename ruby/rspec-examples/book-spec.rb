#test book
require_relative 'book'

describe Book do

	before :each do
		@book = Book.new "Cat's Cradle", "Kurt Vonnegut", :fiction
	end

	describe '#new' do 
		it "should take 3 params and returns a book" do
			expect(@book).to be_an_instance_of Book
		end
	end 

	describe "#title" do
		it "should return the title" do
			expect(@book.title).to eql "Cat's Cradle" 
		end
	end

	describe "#author" do
		it "should return the author" do
			expect(@book.author).to eql "Kurt Vonnegut"
		end
	end

	describe "#category" do
		it "should return the category" do
			expect(@book.category).to eql :fiction
		end
	end

end
