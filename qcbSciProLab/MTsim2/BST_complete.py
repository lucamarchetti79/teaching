class BinaryTree:
    def __init__(self, value):
        self.__data = value
        self.__right = None
        self.__left = None
        self.__parent = None
        self.__depth = 0
    
    def getDepth(self):
        return self.__depth    
    def setDepth(self, newdepth):
        self.__depth = newdepth

    def getValue(self):
        return self.__data
    def setValue(self, newValue):
        self.__data = newValue
    
    def getParent(self):
        return self.__parent
    def setParent(self, tree):
        self.__parent = tree
    
    def getRight(self):
        return self.__right
    def getLeft(self):
        return self.__left
    
    def insertRight(self, tree):
        if self.__right == None:
            self.__right = tree
            tree.setParent(self)
            tree.setDepth(self.getDepth() + 1)                
    def insertLeft(self, tree):
        if self.__left == None:
            self.__left = tree
            tree.setDepth(self.getDepth() + 1)
            tree.setParent(self)
            
    def deleteRight(self):
        self.__right = None   
    def deleteLeft(self):
        self.__left = None
        
    def inOrderDFS(self):
        ret = []
        if self != None:
            r = self.getRight()
            l = self.getLeft()
            if l != None:
                ret.extend(l.inOrderDFS())
            ret.append(self.getValue())
            if r != None:
                ret.extend(r.inOrderDFS())
        return ret

    def search_interval(self, a, b):
        # implemented function!
        greaterThanMin = a < self.__data
        lowerThanMax = b > self.__data

        elements = []

        if greaterThanMin:
            if (self.__left != None):
                elements.extend(self.__left.search_interval(a, b))

        if (a <= self.__data <= b):
            elements.append(self.__data)

        if lowerThanMax:
            if (self.__right != None):
                elements.extend(self.__right.search_interval(a, b))

        return(elements)

def createBST(intList):
    BST = None
    if len(intList) > 0:
        BST = BinaryTree(intList[0])
        for el in intList[1:]:
            cur_el = BST
            alreadyPresent = False
            prev_el = None
            while cur_el != None:
                prev_el = cur_el
                cv = cur_el.getValue()
                if  cv > el:
                    cur_el = cur_el.getLeft()
                elif cv < el:
                    cur_el = cur_el.getRight()
                else:
                    # cv == el (el is already present)
                    # not allowed by rule c, so skip it
                    alreadyPresent = True
                    #print("El {} already present".format(el))
                    break
                
            if not alreadyPresent:
                node = BinaryTree(el)
                node.setParent(prev_el)
                if prev_el.getValue() > el:
                    prev_el.insertLeft(node)
                else:
                    prev_el.insertRight(node)
                
    return BST
    

def printTree(root):
    cur = root
    #each element is a node and a depth
    #depth is used to format prints (with tabs)
    nodes = [(cur,0)]
    tabs = ""
    lev = 0
    while len(nodes) >0:
        cur, lev = nodes.pop(-1)
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
    import random

    inList = []
    for i in range(1000):
        inList.append(random.randint(0,1000))
        
    #printTree(createBST(inList[:20])) # to test tree creation...
    
    BST = createBST(inList)
            
    sorted = BST.search_interval(24, 33)
    print("Elements between 24 and 33 in the BST:")
    print(sorted)