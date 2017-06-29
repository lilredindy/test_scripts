# 'ab' is short for 'a'ddress'b'ook

ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
        'Larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com' }
print "Swaroop's address is", ab['Swaroop']
# Deleting a key-value pair
del ab['Spammer']
print 'There are {} contacts in the address-book'.format(len(ab))
for name, address in ab.items():
    print "Contact {} at {}".format(name, address)
for name, address in ab.items():
    print "Contact", name, "at",  address
for items in ab.items():
    print items[0], items[1]

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'
ab['cd'] = (1, 2)
if 'Guido' in ab:
    print "\nGuido's address is {}", ab['Guido']
if 'cd' in ab:
    print "%s%s is cd's addy\n" % ab['cd']



k1 = ("a", "b", "c", "d") #the key can be a tuple
v1 = ["foo", "bar"] 
dict = {k1: v1}
for items in dict.items():
	print items[0], items[1], "\n"



import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_key = sorted(x.items(), key=operator.itemgetter(0))
sorted_val = sorted(x.items(), key=operator.itemgetter(1))
print (sorted_key)
print (sorted_val)




