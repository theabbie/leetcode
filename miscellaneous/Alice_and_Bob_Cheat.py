class Number:
    def primepowers(N, p, mod):
        ip = pow(p, mod - 2, mod)
        pw = 1
        invpw = 1
        ppow = []
        invppow = []
        for _ in range(n):
            ppow.append(pw)
            invppow.append(invpw)
            pw = (pw * p) % mod
            invpw = (invpw * ip) % mod
        return ppow, invppow

class StringHash:
    def __init__(self, s, p, mod):
        self.p = p
        self.mod = mod
        self.ppow, self.invppow = Number.primepowers(len(s) + 1, self.p, self.mod)
        self.hashvals = self.hashes(s)
        
    def hashes(self, s):
        n = len(s)
        h = [0] * (n + 1)
        for i in range(n):
            h[i + 1] = (h[i] + self.ppow[i] * (ord(s[i]) - ord('a'))) % self.mod
        return h
    
    def rangeHash(self, i, j):
        return (self.invppow[i] * (self.hashvals[j + 1] + self.mod - self.hashvals[i])) % self.mod

class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        k = len("{:b}".format(n))
        table = [[float("inf")] * k for _ in range(n)]
        for l in range(k):
            for i in range(n):
                if l == 0:
                    table[i][l] = arr[i]
                else:
                    a = table[i][l - 1]
                    b = float("inf")
                    if i + (1 << l - 1) < n:
                        b = table[i + (1 << l - 1)][l - 1]
                    table[i][l] = min(a, b)
        self.table = table

    def min(self, l, r):
        bits = "{:b}".format(r - l)[::-1]
        res = float("inf")
        for i, b in enumerate(bits):
            if b == "1":
                res = min(res, self.table[l][i])
                l += 1 << i
        return res

t = int(input())

n = int(input())

s = input()

a = list(map(int, input().split()))

p = [0] * (n + 1)

for i in range(n):
    p[i + 1] += p[i] + a[i]

ahash = StringHash(s, 31, 10 ** 9 + 7)
bhash = StringHash(s, 37, 10 ** 9 + 9)

pquery = SparseTable(p)

print(p)

res = 0

for i in range(n - 1):
    beg = 1
    end = i + 1
    res = 0
    while beg <= end:
        mid = (beg + end) // 2
        if (ahash.rangeHash(i - mid + 1, i), bhash.rangeHash(i - mid + 1, i)) == (ahash.rangeHash(n - mid, n - 1), bhash.rangeHash(n - mid, n - 1)):
            res = mid
            beg = mid + 1
        else:
            end = mid - 1
    res = max(res, p[n] - pquery.min(n - res, n + 1), p[i + 1] - pquery.min(i + 1 - res, i + 2))

print(res)