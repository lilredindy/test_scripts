
def mtdarry  
	var1 = ['test']
  10.times do |num|  
    square = num * num  
    return num, square if num > 5
    #var1 << square
  end  
  puts var1
end  
  
# using parallel assignment to collect the return value  
#num, square = mtdarry  
#puts num  
#puts square


puts mtdarry

=begin
#var2 = ['a' 'b']
mtdarry.each do |var3|
	puts var3
end
=end
