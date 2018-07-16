#this is too hard
#i would need like 2 weeks to even start to think about this type of problem

import urllib2  # the lib that handles the url stuff
import itertools
import ast


target_url = " https://keybase.io/jobs/q/e5b78ebaabe9f21b?page=data"
data = urllib2.urlopen(target_url) # it's a file like object and works just like a file

L = []


for line in data: # files are iterable
    if "follows" in line:
		d = ast.literal_eval(line.strip().strip(','))
		

		d['score'] = 0
		if 'pgp' in d:
			d['score'] += 1
		if 'twitter' in d:
			d['score'] += 1
		if 'reddit' in d:
			d['score'] += 1		
		if 'hackernews' in d:
			d['score'] += 1
		if 'github' in d:
			d['score'] += 1

		#print d
		L.append(d)
		


list_of_triples = []	

triple  = None

for d in L:
	if (triple):
		pass
	else:
		triple = dict()
		triple['people'] = []
		triple['quality'] = ""


	if len(triple['people']) == 3:
		list_of_triples.append(triple)
		triple = None
	else:
		triple['people'].append(d['keybase'])


for t in list_of_triples:
	print t

