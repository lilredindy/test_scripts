class AddableDict(dict):

    def __add__(self, otherObj):
        self.update(otherObj)
        return AddableDict(self)


dict1 = AddableDict({1 : "ABC"})
dict2 = AddableDict({2 : "EFG"})
print (dict1 + dict2)


dict3 = {3 : "HIJ"}
dict4 = {4 : "KLM"}
#print dict3 + dict4

list = [4,2,1,-1,3,9,-1]
print any([x > 0 for x in list])
print all([x > 0 for x in list])
