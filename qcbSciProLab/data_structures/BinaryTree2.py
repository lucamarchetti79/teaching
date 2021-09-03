class BinaryTree:
    def __init__(self, value):
        self.__data = value
        self.__right = None
        self.__left = None
        self.__parent = None
        self.__depth = 0 # new param

    def getValue(self):
        return self.__data
    def setValue(self, newval):
        self.__data = newval

    def getParent(self):
        return self.__parent
    def setParent(self, tree):
        self.__parent = tree

    def getRight(self):
        return self.__right
    def getLeft(self):
        return self.__left

     # new method
    def getDepth(self):
        return self.__depth
    # new method
    def setDepth(self, newdepth):
        self.__depth = newdepth


    def insertRight(self, tree):
        if self.__right == None:
            self.__right = tree
            tree.setParent(self)
            #line modified
            tree.setDepth(self.getDepth() + 1)

    def insertLeft(self, tree):
        if self.__left == None:
            self.__left = tree
            #line modified
            tree.setDepth(self.getDepth() + 1)
            tree.setParent(self)

    def deleteRight(self):
        self.__right = None

    def deleteLeft(self):
        self.__left = None



def printTree(root):
    cur = root
    #each element is a node and a depth
    #depth is used to format prints (with tabs)
    nodes = [(cur,0)]
    tabs = ""
    lev = 0
    while len(nodes) >0:
        cur, lev = nodes.pop(-1)
        #print("{}{}".format("\t"*lev, cur.getValue()))
        if cur.getRight() != None:
            print ("{}{} (r)-> {}".format("\t"*lev,
                                          cur.getValue(),
                                          cur.getRight().getValue()))
            nodes.append((cur.getRight(), lev+1))
        if cur.getLeft() != None:
            print ("{}{} (l)-> {}".format("\t"*lev,
                                          cur.getValue(),
                                          cur.getLeft().getValue()))
            nodes.append((cur.getLeft(), lev+1))

if __name__ == "__main__":
    BT = BinaryTree("Root")
    bt1 = BinaryTree(1)
    bt2 = BinaryTree(2)
    bt3 = BinaryTree(3)
    bt4 = BinaryTree(4)
    bt5 = BinaryTree(5)
    bt6 = BinaryTree(6)
    bt5a = BinaryTree("5a")
    bt5b = BinaryTree("5b")
    bt5c = BinaryTree("5c")
    bt7 = BinaryTree(7)
    bt8 = BinaryTree(8)
    BT.insertLeft(bt1)
    BT.insertRight(bt2)
    bt2.insertLeft(bt3)
    bt3.insertLeft(bt4)
    bt3.insertRight(bt5)
    bt2.insertRight(bt6)
    bt1.insertRight(bt5b)
    bt1.insertLeft(bt5a)
    bt5b.insertRight(bt5c)
    bt4.insertRight(bt7)
    bt4.insertLeft(bt8)

    nodeList = [BT,bt1,bt2,bt3,bt4, bt5, bt5a, bt5b,
                bt5c, bt6, bt7, bt8]
    for node in nodeList:
        if node != None:
            print("Node {} has depth: {}".format(node.getValue(),
                                                 node.getDepth()))
