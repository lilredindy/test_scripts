
sucks = "sucks"
map = {"old bridge": sucks,  "nj": sucks, "chris christoff": sucks}

print map
print map["old bridge"]
for key, value in map.items():
	print "%s %s" % (key, value) 

print "-------------------------"

def make_complex(*args):
	"""makes shit very complex...like why corporate america has ruined everything"""
	x, y = args
	return dict(**locals())
	
print make_complex("jobs", 2)

print "-------------------------"

foo = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

for key in foo:
	print foo[key]

for (index, key) in enumerate(foo):
	print index, key, foo[key]

for (key, value) in foo.items():
	print key, value

print "-------------------------"

foo = [23,2,2,1]
bar = [i +3 for i in foo if i < 5 ]
print bar

print "-------------------------"

a= 4
b = 'fff'
bar = [a if True == False else b]
print bar


print "-------------------------"

a = [2,45,3]
#a.reverse()
#print a
print a[::-1]

