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

def make_chocolate(small, big, goal):
  

  a = big - (goal / 5) 
  print a
  a_abs = abs (a)
  b = goal % 5
  print b
  c= goal - (big * 5) 
  print c
  if (a == 0):
  	if (b == 0):
  		return 0
  	elif (b > 0 and small >= b):
  		return b
  	else:
  		return -1
  elif a > 0:
    if (goal % 5 <= small):
      return b
    else:
      return -1
  else:
    if (small / 5 >= a_abs and small >= c):
       return c 
    else:
      return -1


print make_chocolate(6,1,12)


print "---------------------------"

str = "fbdd"

for i in range (len(str)):
	print str[0:i+1]