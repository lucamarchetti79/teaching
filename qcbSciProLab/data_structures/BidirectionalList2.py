class Node:
    def __init__(self, data):
        self.__data = data
        self.__prevEl = None
        self.__nextEl = None

    def getData(self):
        return self.__data
    def setData(self, newdata):
        self.__data = newdata

    # next element
    def setNext(self, node):
        self.__nextEl = node
    def getNext(self):
        return self.__nextEl

    # previous element
    def setPrev(self,node):
        self.__prevEl = node
    def getPrev(self):
        return self.__prevEl

    def __str__(self):
        return str(self.__data)

    # for sorting
    def __lt__(self, other):
        return self.__data < other.__data


class BiLinkList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0
        # to reduce complexity of min and max calculation, we keep track 
        # of this information during insertions
        self.__minEl = None # this assumes that nodes can be sorted
        self.__maxEl = None # this assumes that nodes can be sorted

    def __len__(self):
        return self.__len
    def min(self):
        return self.__minEl
    def max(self):
        return self.__maxEl

    def append(self,node):
        if type(node) != Node:
            raise TypeError("node is not of type Node")
        else:
            if self.__head == None:
                self.__head = node
                self.__tail = node
            else:
                node.setPrev(self.__tail)
                self.__tail.setNext(node)
                self.__tail = node
            self.__len += 1
            # this assumes that nodes can be sorted
            if self.__minEl == None or self.__minEl > node:
                self.__minEl = node
            if self.__maxEl == None or self.__maxEl < node:
                self.__maxEl = node

    def insert(self, node, i):
        # to avoid index problems, if i is out of bounds
        # we insert at beginning or end
        if i > self.__len:
            i = self.__len #I know that it is after tail!
        if i < 0:
            i = 0
        cnt = 0
        cur_el = self.__head
        while cnt < i:
            cur_el = cur_el.getNext()
            cnt += 1
        #add node before cur_el
        if cur_el == self.__head:
            #add before current head
            node.setNext(self.__head)
            self.__head.setPrev(node)
            self.__head = node
        else:
            if cur_el == None:
                #add after tail
                self.__tail.setNext(node)
                node.setPrev(self.__tail)
                self.__tail = node
            else:
                #add in the middle of the list
                p = cur_el.getPrev()
                p.setNext(node)
                node.setPrev(p)
                node.setNext(cur_el)
                cur_el.setPrev(node)

        self.__len += 1
        #This assumes that nodes can be sorted
        if self.__minEl == None or self.__minEl > node:
            self.__minEl = node
        if self.__maxEl == None or self.__maxEl < node:
            self.__maxEl = node

    def getAtIndex(self, i):
        if i > self.__len:
            return None
        else:
            cnt = 0
            cur_el = self.__head
            while cnt < self.__len:
                if cnt == i:
                    return cur_el
                else:
                    cnt += 1
                    cur_el = cur_el.getNext()

    def iterator(self):
        cur_el = self.__head
        while cur_el != None:
            yield cur_el
            cur_el = cur_el.getNext()

    def __str__(self):
        if self.__head != None:
            dta = str(self.__head)
            cur_el = self.__head.getNext()
            while cur_el != None:
                dta += " <-> " + str(cur_el)
                cur_el = cur_el.getNext()

            return str(dta)
        else:
            return ""
    
    ###################################################
    ################### NEW METHODS ###################
    #  WARINING: these implementations do not update 
    #          self.__minEl and self.__maxEl
    ###################################################
    def remove(self, element):
        # WARNING: this implementation does not update self.__minEl and self.__maxEl
        if self.__head != None:
            cur_el = self.__head
            while cur_el != element and cur_el != None:
                cur_el = cur_el.getNext()

            if cur_el != None:
                p = cur_el.getPrev()
                n = cur_el.getNext()

                if cur_el == self.__head:
                    self.__head = n

                if cur_el == self.__tail:
                    self.__tail = p

                if n != None:
                    n.setPrev(p)
                if p != None:
                    p.setNext(n)
                    
                self.__len -= 1

            
    def slice(self, x, y):
        m = min(x,y)
        M = max(x,y)
        
        if m > self.__len:
            return None
        else:
            cur_el = self.__head
            cnt = 0
            while cnt < m:
                cur_el = cur_el.getNext()
                cnt += 1
            nList = BiLinkList()
            
            while cnt < M and cur_el != None:
                    n = Node(cur_el.getData())
                    cur_el = cur_el.getNext()
                    nList.append(n)
                    cnt += 1
            return nList
    
    ###################################################
    ############### END NEW METHODS ###################
    ###################################################

if __name__ == "__main__":
    import random
    MLL = BiLinkList()
    for i in range(1,50,10):
        n = Node(i)
        MLL.append(n)
    print(MLL)
    for el in MLL.iterator():
        print("\t{} prev:{} next:{}".format(el,el.getPrev(), 
                                            el.getNext()))
    n = Node(2)
    MLL.insert(n,2)
    n = Node(-10)
    MLL.append(n)
    n = Node(1000)
    MLL.insert(n, -1)
    n = Node(27)
    MLL.insert(n, 2000)
    
    print(MLL)
    for el in MLL.iterator():
        print("\t{} prev:{} next:{}".format(el,el.getPrev(), 
                                            el.getNext()))
    print("Number of elements: {} min: {}  max: {}".format(len(MLL),
                                                           MLL.min(), 
                                                           MLL.max()))
    n = MLL.getAtIndex(3)
    print("MLL[3] = {}".format(n))
    MLL.remove(n)
    print("{} removed!".format(n))
    print(MLL)
    for el in MLL.iterator():
        print("\t{} prev:{} next:{}".format(el,el.getPrev(), 
                                            el.getNext()))
    
    n = MLL.getAtIndex(0)
    print("MLL[0] = {}".format(n))
    MLL.remove(n)
    print("{} removed!".format(n))
    print(MLL)
    
    for el in MLL.iterator():
        print("\t{} prev:{} next:{}".format(el,el.getPrev(), 
                                            el.getNext()))
        
    #slice:
    print("Slice[2,4]:")
    print(MLL.slice(2,4))

    #slice:
    print("Slice[3,15]:")
    print(MLL.slice(3,15))
    
    #Removing all elements now.
    print("Remove all")
    for i in range(len(MLL)):
        n = MLL.getAtIndex(0)
        MLL.remove(n)
        print("{} removed!".format(n))
        print(MLL)
    print("Current list content:", MLL)
    