[1,2,3].each { |num| print "#{num}! \n" }

puts "\n----------------"

["Cool", "chicken!", "beans!", "beef!"].each_with_index do |item, index|
	print "#{item} " if index%2==0
end

puts "\n----------------"

my_array = [2,3,0,1,2.3,8,22]
array1 = my_array.select{|item| item%2==0 }
print array1

puts "\n-----------------"

array2 = my_array.select do |item| 
	item%3==0 
end
print array2

