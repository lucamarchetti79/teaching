class SortingAlgorithm:
    def __init__(self, data, verbose = True):
        self.data = data
        self.comparisons = 0
        self.operations = 0
        self.verbose = verbose

    def getData(self):
        return self.data

    def getOperations(self):
        return self.operations

    def getComparisons(self):
        return self.comparisons

    def sort(self):
        raise NotImplementedError

sa = SortingAlgorithm([])
print(sa)
sa.sort()