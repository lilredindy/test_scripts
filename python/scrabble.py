import sys

a = 'aabbacracadabra'
b = list(a)
#print b
b.remove('c')
#print b


scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def words_that_match(f, rack):
	words = list(f)
	valid_words = []

	for word in words:
		word = word.strip('\n')
		w = list(word)

		for l in rack:
			if l in w:
				w.remove(l)
			if len(w) is 0: 
				valid_words.append(word)
				#print "found %s" % word
				break

	return valid_words


try:
	rack = sys.argv[1]
	f = open('sowpods.txt', 'r')

	valid_words = words_that_match(f, rack)
	scoring = {}
	
	for word in valid_words:
		score = 0
		w = list(word)
		for l in w:
			score += scores[l.lower()]
		scoring[word] = score

	print scoring

	f.close()
except IndexError:
	print "no rack provided"
	exit()
