class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

def numres(constraints, n):
    dsu = UnionFind(n)
    for i in range(n):
        same = False
        for j in range(n - 1, i - 1, -1):
            if constraints[i][j] == 1:
                same = True
            if constraints[i][j] == 2:
                if same or i == j:
                    return 0
            if same:
                dsu.union(i, j)
    res = 0
    for i in range(n):
        ctr = 0
        for j in range(n - 1, i - 1, -1):
            if dsu.find(i) == i:
                ctr += 1
        res += (1 << ctr) - 1
    return res

n = int(input())

constraints = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    curr = list(map(int, input().split()))
    for j in range(n - i):
        constraints[i][i + j] = curr[j]
        constraints[i + j][i] = curr[j]

print(numres(constraints, n) % 998244353)