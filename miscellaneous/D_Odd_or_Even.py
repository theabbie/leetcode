import sys

sys.setrecursionlimit(10 ** 5)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
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

n, k = map(int, input().split())

res = [0] * n

dsu = DSU(n)

prev = 0

curr = list(range(1, k))

for i in range(k - 1, n):
    print("?", *(curr + [i + 1]))
    curr = int(input())
    if i > k - 1:
        if curr != prev:
            res[i] = 1
    prev = curr

prev = 0

for i in range(k - 1):

groups = [[] for _ in range(n)]

for i in range(n):
    groups[dsu.find(i)].append(i)

print(groups)

print("!", *res)