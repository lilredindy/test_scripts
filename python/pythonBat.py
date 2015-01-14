def double_char(str):
  
  a = []
  for i in list(str):
    a.append(i)
    a.append(i)
  
  return ''.join(a)


print double_char("423423")

print "-------------------------------"

def string_match(a, b):
  
  if (len(a) < 2):
  	return 0

  if (len(a) > len(b)):
    length = len(a)
  else:
    length = len(b)
  count = 0
  for i in range(0, length-1):
    if ((a[i] == b[i]) and (a[i+1] == b[i+1])):
      count += 1
  return count

print string_match("z", "z")