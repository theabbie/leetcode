class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        self.expand(nestedList)
        self.i = 0
        
    def expand(self, nestedList):
        for nl in nestedList:
            if nl.isInteger():
                self.arr += [nl.getInteger()]
            else:
                self.expand(nl.getList())
    
    def next(self) -> int:
        self.i += 1
        return self.arr[self.i - 1]
    
    def hasNext(self) -> bool:
        return self.i < len(self.arr)