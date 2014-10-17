#test for library class
require_relative 'library'
require_relative 'book'
require 'yaml'


describe Library do

	before :all do
		  lib_arr = [
            Book.new("JavaScript: The Good Parts", "Douglas Crockford", :development),
            Book.new("Designing with Web Standards", "Jeffrey Zeldman", :design),
            Book.new("Don't Make me Think", "Steve Krug", :usability),
            Book.new("JavaScript Patterns", "Stoyan Stefanov", :development),
            Book.new("Responsive Web Design", "Ethan Marcotte", :design)
        ]

        File.open "books.yaml", "w" do |f|
        	f.write YAML::dump lib_arr
        end
    end

    before :each do
    	@lib = Library.new "books.yaml"
    end


    describe "#new" do

    	context "with 0 params" do
    		it "should have no books" do
    			lib = Library.new
    			lib.should have(0).books
    		end
    	end

    	context "with yaml file param" do
    		it "should have 5 books" do
    			@lib.should have(5).books
    		end
    	end
    end

    describe '#get_books_in_category' do
    	it 'should return all the books in each category' do
    		@lib.get_books_in_category(:development).should have(2).books
    	end
    end

end