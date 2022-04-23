from collections import defaultdict

class Solution:
    def getParent(self, parent, x):
        if parent[x] == x:
            return x
        parent[x] = self.getParent(parent, parent[x])
        return parent[x]
    
    def connect(self, parent, a, b):
        parent[self.getParent(parent, a)] = self.getParent(parent, b)
        
    def isConnected(self, parent, a, b):
        return self.getParent(parent, a) == self.getParent(parent, b)
    
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = list(range(n))
        meets = defaultdict(list)
        for a, b, t in meetings:
            meets[t].append((a, b))
        self.connect(parent, 0, firstPerson)
        people = set()
        for t in sorted(meets.keys()):
            people.clear()
            for a, b in meets[t]:
                self.connect(parent, a, b)
                people.update({a, b})
            for p in people:
                if not self.isConnected(parent, p, 0):
                    parent[p] = p
        return [i for i in range(n) if self.isConnected(parent, i, 0)]