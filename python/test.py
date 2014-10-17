#this is my python scrip

x = 4
if (x > 2):
	print ("shit u won")
elif (x == 2):
	print ("x is less than 2")
else:
	print ('you wasteed time')


def foo():
	a = 2
	b = 3
	print(a + b)

def bar(a, b):
	for c in range(a,b):
		print (c)	

def gat(str, a,b):
	print(str[a:b])

def cats_list():
	cats = ['bob', 'home', 'ran', 'fan', 1, 2,-1,345]
	cats.sort()
	for i in cats:
		print i

def cats_tuple():
	cats = ('bob', 'home', 'ran', 'fan', 1, 2,-1,345)
	print (cats[0],cats[3])
	for i in cats:
		print i

def cats_dict():
	cats = {'cat1':'bob', 'cat2': 'john', 'cat3': 'ok', 'cat5': 6}
	print(cats['cat1'],cats['cat2'])
	for i in cats:
		print (i,cats[i])

def dog():
	str = 'abcdefghijklmnop'
	print('this is my string %s' % str)
	print('this is my string %.2s' % str)

def bird():
	try:
		str = 'bird'
		str = str + 1
	except: print(str, "can't add a bird to a number")
	print('but you can add a bird to the sky')



def falcon():
	try:
		str = 'bird'
		x = '1'
		str = str + x
		print (str)
	except:
		print('but you can add a bird to the sky')

def reed(path):
	f = open(path, "r")
	lineList = []
	for line in f:
		lineList.append(line)
	print(lineList)
	f.close()
	f = open(path, "r")
	print(f.readline())
	print(	f.read(12))
	f.close()


def wright(path):
	f = open(path, "a")
	f.write("last word is now\n")
	f.close()

class Calc():
	def __init__(self):
		print("in the Calc class")
	def add(self,x,y):
		print(x + y)
	def subtract(self,x,y):
		print(x - y)

foo()
bar(3, 10)
gat('onomonopetia', 10, -1)
gat('onomonopetia', 0, 3)
cats_list()
cats_tuple()
cats_dict()
dog()
bird()
falcon()
reed('C:\\Documents and Settings\\chuck\Desktop\\shri\\Development\\python_scripts\\test.txt')
wright('C:\\Documents and Settings\\chuck\Desktop\\shri\\Development\\python_scripts\\test.txt')
c =  Calc()
c.add(4,5) #should be 9
c.subtract(9,5) #should be 4
