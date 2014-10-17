def call_block  
	puts 'Start of method'  
  	# you can call the block using the yield keyword  
  	if block_given?
  		yield  
  		yield  
  	end
  	puts 'End of method'  
end 

call_block {puts "hello world"}