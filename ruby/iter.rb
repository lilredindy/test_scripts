

a_list = [3,2,2,5,1]
b_list = [7,5,88,6]
c_list = [0.9,0.78,0.43]

a_list.each do |a|
	puts a
	a_list = [55,43,2]
end


a_list.each do |a|
	puts a
end


b_list.each_with_index do |b,i|
	puts b_list[i]
	b_list = [34,23,25,50]
end

for c in c_list
	puts c
	c_list = [56,45]
end
