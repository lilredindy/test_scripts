def double_char(str):
  
  a = []
  for i in list(str):
    a.append(i)
    a.append(i)
  
  return ''.join(a)


print double_char("423423")

print "-------------------------------"

'''
/html/body/div[3]/div/div[2]/a
/html/body/div[3]/div/div[2]/a

/html/body/div[3]/div/div[8]/div/form/div/input[1]
/html/body/div[3]/div/div[8]/div/form/div/input[1]

css selector notation 1: "input#email.required.email"
css selector notation 2: "input[id=email]"
'''

def centered_average(nums):
	min_num = nums[0]
	max_num = nums[0]

	for i in nums:
		if (i > max_num):
			max_num = i
		if (i < min_num):
			min_num = i
	
	


centered_average([2,2,2,222,2])

foo = 23232323

print foo[3]


  