class MyStack:

    def __init__(self):
        self.__data = list()

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
            return self.__data.pop()
        else:
            return None

    def peek(self):
        if len(self.__data) > 0:
            return self.__data[-1]
        else:
            return None

if __name__ == "__main__":
    S = MyStack()
    print("Is it empty? {}".format(S.isEmpty()))
    print("Initial length: {}".format(len(S)))
    S.push("[1,2,3]")
    print("Added [1,2,3]")
    S.push("[4,5,6]")
    print("Added [4,5,6]")
    print("Is it empty? {}".format(S.isEmpty()))
    S.push([1,4,5])
    print("Added [1,4,5]")
    print("On top of the stack: {}".format(S.peek()))
    print("Let's start removing elements...")
    print("On top of the stack: {}".format(S.pop()))
    print("On top of the stack: {}".format(S.pop()))
    print("On top of the stack: {}".format(S.pop()))
    print("On top of the stack: {}".format(S.pop()))
    S.push(123456)
    print("Added 123456")
    print("On top of the stack: {}".format(S.pop()))
    print("On top of the stack: {}".format(S.pop()))
