#this is too hard
#i would need like 2 weeks to even start to think about this type of problem

import urllib2  # the lib that handles the url stuff
import itertools
import ast
import time


def calc_quality(triple, hash_tbl):
	
	score = 0
	for x in triple:
		score += hash_tbl[x]['score']
	#print score

	if (triple[0] in hash_tbl[triple[1]]['follows']):
		score *=2
	if (triple[0] in hash_tbl[triple[2]]['follows']):
		score *=2
	if (triple[1] in hash_tbl[triple[0]]['follows']):
		score *=2
	if (triple[1] in hash_tbl[triple[2]]['follows']):
		score *=2
	if (triple[2] in hash_tbl[triple[0]]['follows']):
		score *=2
	if (triple[2] in hash_tbl[triple[1]]['follows']):
		score *=2
	#print score

	return {'people': triple, 'quality': score}



def make_triples(hash_tbl):

	list_of_triples = []	
	triple = []

	for key in hash_tbl: 
		
		if not hash_tbl[key]['usedIt']: ##not sequential iteration so we need to check here
			triple.append(key) 
			hash_tbl[key]['usedIt'] = True
		

			for k in hash_tbl[key]['follows']:
				if (len(triple) == 3):
					break
				if not hash_tbl[k]['usedIt']:
						triple.append(k) 
						hash_tbl[k]['usedIt'] = True
							


		if (len(triple) == 3):
			#print triple
			triple_with_quality = calc_quality(triple, hash_tbl)
			list_of_triples.append(triple_with_quality)
			triple = []	 #reset the list	

	return list_of_triples

	'''
			if (len(triple) < 3):
				if hash_tbl[key]['follows']:
					key = hash_tbl[key]['follows'][0]
					if not hash_tbl[key]['usedIt']:
						triple.append(key) 
						hash_tbl[key]['usedIt'] = True

						if (len(triple) < 3):
							if hash_tbl[key]['follows']:
								key = hash_tbl[key]['follows'][0]
								if not hash_tbl[key]['usedIt']:
									triple.append(key) 
									hash_tbl[key]['usedIt'] = True


		if (len(triple) == 3):
			print triple
			triple_with_quality_set = calc_quality(triple, hash_tbl)
			list_of_triples_with_quality_set.append(triple_with_quality_set)
			triple = []
	'''

start_time = time.time()

target_url = "https://keybase.io/jobs/q/e5b78ebaabe9f21b?page=data"
data = urllib2.urlopen(target_url) # it's a file like object and works just like a file
D = dict()

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

		d['usedIt'] = False


		D[d['keybase']] = d #make hash table

print len(D)
#print D
#print D['jz']['follows']
triples_dict = make_triples(D)
for t in triples_dict:
	print t
print("--- %s seconds ---" % (time.time() - start_time))








