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

if __name__ == "__main__":
    import random
    MLL = BiLinkList()
    for i in range(1,50,10):
        n = Node(i)
        MLL.append(n)
    print(MLL)
    for el in MLL.iterator():
        print("\t{} prev:{} next:{}".format(el,
                                            el.getPrev(),
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
        print("\t{} prev:{} next:{}".format(el,
                                            el.getPrev(),
                                            el.getNext()))
    print("Number of elements: {} min: {}  max: {}".format(len(MLL),
                                                           MLL.min(),
                                                           MLL.max()))
    N = MLL.getAtIndex(4)
    print("MLL[4] = {}".format(N))
    for i in range(3):
        print("Moving backwards {} steps from {}".format(i+1, N))
        print("\tI find node: {}".format(N.getPrev()))
        N = N.getPrev()