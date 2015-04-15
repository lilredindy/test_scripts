string1 = "sussingt"
string2 = "tungisss"



#this is the anagram algorithm 
#time-complexity is O(2n)
d1 = dict()
d2 = dict()

for i in string1:
	if (i in d1.keys()):
		d1[i] = d1[i] + 1
	else:
		d1[i] = 1

for i in string2:
	if (i in d2.keys()):
		d2[i] = d2[i] + 1
	else:
		d2[i] = 1



#method 1 for equality
print "--------------------------------"
print d1
print d2
if (d1 == d2):
	print 'same'
if (d1 is not d2):
	print 'identities are not same' 


#method 2 for equality
print "-----------------------------------"
for str1_values, str2_values in zip(d1.iteritems(), d2.iteritems()):
        if str1_values == str2_values:
            print 'Ok', str1_values, str2_values
        else:
            print 'Fail', str1_values, str2_values



#method 3 for equality (items() vs iteritems())
print "---------------------------"
for items in d1.iteritems():
	print items
print d1.items()
shared_items = set(d1.items()) ^ set(d2.items())
print shared_items




#below is just random python testing
print "--------------------------------"



#iteritems() works 2 ways
#unpacks as tuple or,
#unpacks as key, value
a = dict(a=1, b=2,c=3)
for k in a.iteritems():
	print k 



#tuple's are "immutable", but can do this??
t = (1,1,2,2,2)
print t
t = t  + (2,2,2)
print t


#why lists don't work, b/c order is important
string1 = "sussingt"
string2 = "tungisss"

d1 = dict()
d2 = dict()
l1 = list()
l2 = list()
for i in string1:
	 l1.append(i)

for j in string2:
	l2.append(j)

print l1, l2
print l1 == l2