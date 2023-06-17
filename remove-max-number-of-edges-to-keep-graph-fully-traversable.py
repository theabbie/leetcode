class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.numsets = n
        
    def find(self, a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.size[parent_a] < self.size[parent_b]:
                parent_a, parent_b = parent_b, parent_a
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]
            self.numsets -= 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU(n)
        bob = DSU(n)
        used = 0
        for t, a, b in edges:
            a -= 1
            b -= 1
            if t == 3:
                if alice.find(a) != alice.find(b) and bob.find(a) != bob.find(b):
                    alice.union(a, b)
                    bob.union(a, b)
                    used += 1
        for t, a, b in edges:
            a -= 1
            b -= 1
            if t == 1:
                if alice.find(a) != alice.find(b):
                    alice.union(a, b)
                    used += 1
            if t == 2:
                if bob.find(a) != bob.find(b):
                    bob.union(a, b)
                    used += 1
            if alice.numsets == 1 and bob.numsets == 1:
                return len(edges) - used
        return -1