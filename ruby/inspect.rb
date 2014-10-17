def foo(*my_string)  
  my_string.inspect  
end  

puts foo('hello','world')  
puts foo()


def bar *params
	params[0] + params[1] + params[2]
end

puts bar('a', 'b', 'c')