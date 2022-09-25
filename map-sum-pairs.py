class Node:
    def __init__(self):
        self.child = {}
        self.total = 0
        self.end = False

class MapSum:
    def __init__(self):
        self.root = Node()
        self.val = {}
        
    def exists(self, s):
        curr = self.root
        for c in key:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.end

    def insert(self, key: str, val: int) -> None:
        self.val[key], val = val, val - self.val.get(key, 0)
        curr = self.root
        curr.total += val
        for c in key:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
            curr.total += val
        curr.end = True

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.child:
                return 0
            curr = curr.child[c]
        return curr.total