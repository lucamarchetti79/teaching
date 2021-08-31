class MyStack:
    
    def __init__(self):
        self.__data = []
    
    def isEmpty(self):
        return len(self.__data) == 0
    
    def __len__(self):
        return len(self.__data)
    
    def push(self, element):
        """adds an element on top of the stack"""
        self.__data.append(element)
        
    def pop(self):
        """removes one element from the stack and returns it"""
        if len(self.__data) > 0:
            ret = self.__data[-1]
            del self.__data[-1]
            return ret
        else:
            return None
    
    def peek(self):
        if len(self.__data) > 0:
            return self.__data[-1]
        else:
            return None
        

def evaluatePostfix(expr):        
    S = MyStack()
    els = expr.split(" ")
    res = 0
    infix = ""
    for i in range(len(els)):
        e = els[i]
        if e not in "+-*/":
            S.push(int(e))
        else:
            o2 = S.pop()
            o1 = S.pop()
            tmp = 0
            infix = "(" + str(o1) + " " + e +" " + str(o2) + ")"  
            print(infix)
            if e == "+":
                tmp = o1 + o2
            
            elif e == "-":
                tmp = o1 - o2
            
            elif e == "/":
                tmp = o1 / o2
            
            else:
                tmp = o1 * o2
            res = tmp
                        
            if i != len(els):
                S.push(res)
    return res


operations = ["10 5 + 7 *", 
              "1 2 3 4 5 6 7 8 + + + + + + +", 
              "1 2 3 4 5 + - * /",
              "5 4 + 8 /",
              "3 10 2 - 5 * +"]

for op in operations:
    print("Operation: {}".format(op))
    res = evaluatePostfix(op)
    print("Result: {}".format(res))
