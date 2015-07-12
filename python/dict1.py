# 'ab' is short for 'a'ddress'b'ook

ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
        'Larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com'
    }

print "Swaroop's address is", ab['Swaroop']

# Deleting a key-value pair
del ab['Spammer']

print '\nThere are {} contacts in the address-book\n'.format(len(ab))

for name, address in ab.items():
    print "Contact {} at {}".format(name, address)

for name, address in ab.items():
    print "Contact", name, "at",  address

for items in ab.items():
    print items[0], items[1]

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'
ab['dickhead'] = (1, 2)

if 'Guido' in ab:
    print "\nGuido's address is {}", ab['Guido']

if 'dickhead' in ab:
    print "\n\n\n%s%s is dickhead's addy" % ab['dickhead']



k1 = ("a", "b", "c", "d") #
v1 = ["foo", "bar"]

dict = {k1: v1}

for items in dict.items():
	print items[0], items[1]



