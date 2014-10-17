def foo (arg) 
	yield(5, 'twist')
	puts "hello #{arg} this is going to be cool"
end

foo ('shri') {|a,b| puts "this is #{a}"; puts "this is #{b}"}





    5.times { puts "Mice!\n" } # more on blocks later  
    puts "Elephants Like Peanuts".length  
    puts self