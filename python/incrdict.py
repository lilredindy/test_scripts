#!/usr/bin/env python
#coding: utf8

#Consider a function incr_dict, which takes two arguments, which behaves like this in Python:
#>>> dct = {} 
#>>> incr_dict(dct, (‘a’, ‘b’, ‘c’)) 
#>>> dct {‘a’: {‘b’: {‘c’: 1}}} 
#>>> incr_dict(dct, (‘a’, ‘b’, ‘c’)) 
#>>> dct {‘a’: {‘b’: {‘c’: 2}}} 
#>>> incr_dict(dct, (‘a’, ‘b’, ‘f’)) 
#>>> dct {‘a’: {‘b’: {‘c’: 2, ‘f’: 1}}} 
#>>> incr_dict(dct, (‘a’, ‘r’, ‘f’)) 
#>>> dct {‘a’: {‘r’: {‘f’: 1}, ‘b’: {‘c’: 2, ‘f’: 1}}} 
#>>> incr_dict(dct, (‘a’, ‘z’)) 
#>>> dct {‘a’: {‘r’: {‘f’: 1}, ‘b’: {‘c’: 2,’f’: 1}, ‘z’: 1}} 
#>>>
#except that it creates any necessary intermediate and leaf nodes. 
#• Implement incr_dict in Python or any language that supports dictionaries. 
#• Write executable tests for your function. 
#• Will your implementation continue to work well if the tuple is extremely long?



def incr_dict(d, T):

	if not T:
		return

	if len(T) == 1:
		if T[0] not in d:
			d[T[0]] = 1
		else:
			d[T[0]] += 1
		return

	if T[0] not in d:
		d[T[0]] = {}
	incr_dict(d[T[0]],T[1:])

	return d
	

T1  = ('a','b','c')
a = incr_dict(dict(),T1)
print (a)
b = incr_dict(a,T1)
print (b)
T2 = ('a', 'b', 'f')
c = incr_dict(b,T2)
print (c)
T3 = ('a', 'r', 'f')
d = incr_dict(c,T3)
print (d)
T4 = ('a', 'z')
e = incr_dict(d,T4)
print (e)


import unittest
class testIncrDict(unittest.TestCase):
	def setUp(self):
		pass
	def test_1(self):
		expected_dict = {'a': {'b': {'c': 1}}}
		self.assertEqual(incr_dict(dict(),('a','b','c')), expected_dict)
	
	def test_2(self):
		expected_dict = {'a': {'b': {'c': 2}}}
		T1  = ('a','b','c')
		a = incr_dict(dict(),T1)
		b = incr_dict(a, T1)
		self.assertEqual(b, expected_dict)
	def tearDown(self):
		pass
 

if __name__ == '__main__':
	unittest.main()
