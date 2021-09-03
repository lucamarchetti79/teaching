class SingleNode:
    def __init__(self, data):
        self.__data = data
        self.__nextEl = None

    def getData(self):
        return self.__data
    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, node):
        self.__nextEl = node
    def getNext(self):
        return self.__nextEl


    def __str__(self):
        return str(self.__data)

    #for sorting
    def __lt__(self, other):
        return self.__data < other.__data

class CircularList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __len__(self):
        return self.__len

    def append(self, node):
        if type(node) != SingleNode:
            raise TypeError("node is not of type SingleNode")
        else:
            if self.__head == None:
                self.__head = node
                self.__tail = node
            else:
                node.setNext(self.__head)
                self.__tail.setNext(node)
                self.__tail = node

            self.__len += 1

    def extend(self, nodesList):
        for el in nodesList:
            self.append(el)

    def head(self):
        return self.__head

    def tail(self):
        return self.__tail

    def get(self, index):
        i = 0
        cur_el = self.__head
        if index < 0:
            #should someone input a very small number!
            while index < 0:
                index = self.__len + index

        while i < index:
            cur_el = cur_el.getNext()
            i += 1
        return cur_el


    def removeAt(self, index):
        i = 0
        cur_el = self.__head
        if index < 0:
            #should someone input a very small number!
            while index < 0:
                index = self.__len + index


        while i < index-1:
            cur_el = cur_el.getNext()
            i += 1
        prev = cur_el
        cur_el = prev.getNext()
        next_el = cur_el.getNext()
        prev.setNext(next_el)
        if cur_el == self.__tail:
            self.__tail = prev
        if cur_el == self.__head:
            self.__head = prev

        self.__len -= 1

    def removeEl(self, element):
        i = 0
        cur_el = self.__head

        while cur_el.getNext() != element and cur_el != self.__tail:
            cur_el = cur_el.getNext()

        if cur_el != self.__tail:
            prev = cur_el
            cur_el = prev.getNext()
            #cur_el is element now
            next_el = cur_el.getNext()
            prev.setNext(next_el)
            if cur_el == self.__tail:
                self.__tail = prev
            if cur_el == self.__head:
                self.__head = prev

            self.__len -= 1

    def __str__(self):
        outStr = ""
        cur_el = self.__head
        outStr = str(cur_el)
        while cur_el != self.__tail:
            cur_el = cur_el.getNext()
            outStr += "-->" + str(cur_el)
        L = len(outStr)
        outStr += "--|\n^"

        i = 0
        while i < L+1:
            outStr = outStr + "-"
            i += 1
        outStr += "|"

        return outStr

if __name__ == "__main__":
    CL = CircularList()
    n = SingleNode([1])
    n1 = SingleNode(2)
    n2 = SingleNode([3])
    n3 = SingleNode([4])
    n4 = SingleNode(5)
    n5 = SingleNode([6])
    CL.append(n)
    CL.append(n1)
    CL.append(n2)
    CL.extend([n3,n4,n5])
    n = SingleNode("luca")
    CL.append(n)
    print(CL)
    print("CL has length: {}".format(len(CL)))
    print("Head:{}\nTail:{}".format(CL.head(),CL.tail()))
    print("{} is at position: {}".format(CL.get(3),3))
    print("{} is at position: {}".format(CL.get(-10),-10))
    print("{} is at position: {}".format(CL.get(20),20))
    print("{} is at position: {}".format(CL.get(0),0))
    CL.removeAt(2)
    CL.removeAt(5)
    print(CL)
    CL.removeEl(n5)
    print(CL)
    #n is not present!
    CL.removeEl(n)
    print(CL)