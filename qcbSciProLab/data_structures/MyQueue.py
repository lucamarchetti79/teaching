class MyQueue:

    def __init__(self):
        self.__data = list()

    def isEmpty(self):
        return len(self.__data) == 0

    def __len__(self):
        return len(self.__data)

    def enqueue(self, element):
        self.__data.insert(0,element)

    def dequeue(self):
        el = None
        if len(self.__data) > 0:
            el = self.__data.pop()
        return el

    def top(self):
        if len(self.__data) > 0:
            return self.__data[-1]

if __name__ == "__main__":
    import time

    Q = MyQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    print("Size of Q: {}".format(len(Q)))
    Q.enqueue(4)
    Q.enqueue(5)
    print("TOP is now: {}\n".format(Q.top()))
    while not Q.isEmpty():
        el = Q.dequeue()
        print("Removing el {} from queue".format(el))

    start_t = time.time()
    for i in range(400000):
        Q.enqueue(i)
    print("\nQueue has size: {}".format(len(Q)))
    #comment the next 3 lines and see what happens
    while not Q.isEmpty():
        el = Q.dequeue()
    print("\nQueue has size: {}".format(len(Q)))
    end_t = time.time()
    print("\nElapsed time: {:.2f}s".format(end_t - start_t))