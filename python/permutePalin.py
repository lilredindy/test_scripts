import itertools

def permuteString(s):
	return list(itertools.permutations(s))


def solution(s):

	#print (list(itertools.permutations(s))
	#print (sorted(s))

	n = int(len(s)/2)
	print (n)


	"""
	for i in range(n):
		print (s[i])
		if s[i] not in s[i+1:]:
			return False
	return True
	"""



	"""
	count = 0 
	for i in range(n):
		foundIt = False
		for j in range(i+1,len(s)):
			print (i,s[i],j,s[j])
			if (s[i] == s[j]):
				foundIt = True			
				break
		if not foundIt:
			count += 1
					


	if (count is 0):
		return True
	if (len(s)%2 is not 0 and count is 1):
		return True

	return False
	"""


	"""
	#THIS WORKS!!!!
	count = 0	
	L = (list(s))
	L2 = []
	for item in L:
		if item not in L2:
			L2.append(item)
			c = L.count(item)
			if c % 2 != 0:
				count +=1

	print (L2)
	print (count)



	if (count is 0):
		return True
	if (len(s)%2 is not 0 and count is 1):
		return True

	return False
	"""


	"""	
	#THIS PROB WORKS!!!!
	from collections import Counter
	count = 0
	L = (list(s))
	D = Counter(L)
	print (D)

	total = 0
	odd = 0
	for i,(key,value) in enumerate(D.items()):
		total += value
		if (value is not 2):
			odd += 1


	print (total,odd)

	if (total % 2 == 0):
		return True
	if (odd <= 1):
		return True

	return False
	""" 
	

s0 = "bob"
s1 = "ceracar"
s2 = "aaabbcc" # 1  
s3 = "9be\\oGy[zy[x0i:K1N2IKXXL~N1|*aGHWdnip&X*R<dp>'Iv6d{M`nRyf.aRN1~i?<{6~V@}69xy72T,6q@:NKr9W>go[pMkB6Ky}~M^t+XJlb6a,`++(c=bN{W-c9v9U,<?tqy{N1a[MpN`({>-k53Q.:06W-|9l+R6gJk5VTKE}9c&_',~krWBCQH<}3Mdt>kF=t&+xzk-7Ux^ro:3~_o`RU\\\\goeE9eF:cbN9gRMf6el:erC3{oUe&W+i9LlK6\\" 
print (solution(s0))


#print (sorted("ab/<ab/'c<dc"))