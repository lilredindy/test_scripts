from collections import OrderedDict, Counter

class OrderedCounter(Counter,OrderedDict):
	pass


str = "CAAB"
d = Counter(str)
print(d)

d = OrderedCounter(str)
print (d)

d = OrderedDict()

for s in str:
	if s not in d:
		d[s] =1
	else:
		d[s] +=1
		
print (d)