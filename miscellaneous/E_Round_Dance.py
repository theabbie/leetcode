from collections import defaultdict

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

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dsu = DSU(n)
    graph = defaultdict(set)
    for i in range(n):
        graph[i].add(arr[i] - 1)
        graph[arr[i] - 1].add(i)
        dsu.union(i, arr[i] - 1)
    mx = set()
    components = [set() for _ in range(n)]
    for i in range(n):
        components[dsu.find(i)].add(i)
        mx.add(dsu.find(i))
    mx = len(mx)
    rem = mx
    gone = defaultdict(int)
    for i in range(n):
        for j in components[i]:
            curr = 0
            for k in graph[j]:
                if k in components[i]:
                    curr += 1
            if curr < 2:
                for k in graph[j]:
                    dsu.union(i, )
    print(rem, mx)