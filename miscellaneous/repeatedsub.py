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
                        
s = input()
n = len(s)

ahash = StringHash(s, 31, 10 ** 9 + 7)
bhash = StringHash(s, 37, 10 ** 9 + 9)

beg = 1
end = n
res = -1

while beg <= end:
    mid = (beg + end) // 2
    possible = False
    seen = set()
    for i in range(n - mid + 1):
        curr = (ahash.rangeHash(i, i + mid - 1), bhash.rangeHash(i, i + mid - 1))
        if curr in seen:
            possible = s[i:i+mid]
            break
        seen.add(curr)
    if possible:
        res = possible
        beg = mid + 1
    else:
        end = mid - 1
        
print(res)