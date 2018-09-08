
class Expando(object):
    pass

a = Expando()
a.random = 5            #no class variable required
print(a.random) 



#why i need self as first arg
class C: 
    def __init__(self, format):
        self.format = format

    def process(self,formatting=None):
        formatting = formatting if formatting is not None else self.format
        print(formatting)

    def nonstaticmethod(self):
    	print('hello')

c = C("format string")
c.process()       
c.nonstaticmethod()



class Node:
     def __init__(self, mylist = ['o']):
         self.mylist = mylist
 
a = Node()
b = Node()

a.mylist.append("a")
b.mylist.append("b")
print (a.mylist, b.mylist)



class Node2:
    def __init__(self):
        self.mylist = []

c = Node2()
d = Node2()

c.mylist.append("c")
d.mylist.append("d")
print (c.mylist,d.mylist)




