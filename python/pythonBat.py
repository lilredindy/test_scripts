def last2(str):
  if (len(str) <= 3): return 0
  last_2 = str[-2 :]
  count = 0
  for i in range(len(str)- 2):
    if ((str[i] == last_2[0]) and (str[i + 1] == last_2[-1])):
      count = count +1  
  return count


def array_front9(nums):
  result = ""
  if (len(nums) < 4): 
    result = nums
  else:
    result = nums[0:4] 

  for i in result:
    if (i == 9):
      return True

  return False
  

def array123(nums):
  abc = ['a', 'b', 'c']
  abc.pop(1)
  return abc
print array123(1)


end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6 ,
print end7 + end8 + end9 + end10 + end11 + end12
