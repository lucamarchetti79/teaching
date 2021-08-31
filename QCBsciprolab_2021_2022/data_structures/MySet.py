class MySet:
    def __init__(self, elements):
        self.iteratorPosition = 0
        self.__data = dict()
        for el in elements:
            self.__data[el] = 1
    
    #let's specify the special operator for len
    def __len__(self):
        return len(self.__data)
    
    #this is the special operator for in
    def __contains__(self, element):
        el = self.__data.get(element, None)
        return el != None
        
    #we do not redefine __add__ because that is for S1 + S2
    #where S1 and S2 are sets
    def add(self, element):
        #don't care if already there
        self.__data[element] = 1 
    
    def discard(self, element):
        #equivalent to: 
        #if element in self.__data: del self.__data[element]
        el = self.__data.pop(element, None)
    
    def __iter__(self):
        return self # the object itself will be the iterator...

    def __next__(self):
        if self.iteratorPosition > (len(self.__data) - 1):
            self.iteratorPosition = 0
            raise StopIteration()
        pos = self.iteratorPosition
        self.iteratorPosition += 1
        keys = list(self.__data.keys())
        return keys[pos]
            
    def __str__(self):
        keys = self.__data.keys() 
        return "{"+"{}".format(", ".join([str(x) for x in keys])) + "}"

    def union(self, other):
        """elements in either of the two sets"""
        elements = []
        for el in other:
            elements.append(el)
        S = MySet(elements)
        i=0
        for el in self:
            S.add(el)
        return S

    def intersection(self, other):
        """elements in both sets"""
        """elements in both sets"""
        my_keys = self.__data.keys()
        your_keys = other.__data.keys()
        inter = [x for x in my_keys if x in your_keys]
        return MySet(inter)

    def difference(self, other):
        """elements in self but not in other"""
        diff = [x for x in self if x not in other]
        return MySet(diff)

if __name__ == "__main__":
    S = MySet([33, 1,4,5,7,5,5,5,4,7,3])
    print("Initial S: {}".format(S))
    S.add(125)
    S.discard(77)
    S.discard(5)
    print("S now: {}".format(S))
    print("Does S contain 13? {}".format(13 in S))
    print("Does S contain 125? {}".format(125 in S))
    print("All elements in S:")
    for s in S:
        print("\telement: {}".format(s))

    print("\nS: {}".format(S))
    S1 = MySet([33, 0, 3,4, 4, 33,44])
    print("S1: {}".format(S1))
    print("\nUnion: {}".format(S.union(S1)))
    print("Intersection: {}".format(S.intersection(S1)))
    print("S - S1: {}".format(S.difference(S1)))
    print("S1 - S: {}".format(S1.difference(S)))
    print("(S - S1) U (S1 -S): {}".format(S.difference(S1).union(S1.difference(S))))
    
    #### Test vs python's set
    print("\nTesting python's builtin:")
    pS = set([33, 1,4,5,7,5,5,5,4,7,3])
    pS.add(125)
    #pS.remove(77) # this gives an error!
    pS.remove(5)
    print("pS: {}".format(pS))
    pS1 = set([33, 0, 3,4, 4, 33,44])
    print("pS1: {}".format(pS1))
    print("Union: {}".format(pS | pS1))
    print("Intersection: {}".format(pS & pS1))
    print("pS - pS1: {}".format(pS - pS1))
    print("pS1 - pS: {}".format(pS1 - pS))
    print("(pS - pS1) U (pS1 -pS): {}".format(pS - pS1 | pS1 - pS))
    