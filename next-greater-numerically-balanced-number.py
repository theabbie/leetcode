M1 = 10 ** 9 + 7
M2 = 10 ** 9 + 33
p1 = 10 ** 9 + 9
p2 = 10 ** 9 + 87
pw1 = [1] * 10
pw2 = [1] * 10
for i in range(1, 10):
    pw1[i] = p1 * pw1[i - 1]
    pw2[i] = p2 * pw2[i - 1]
    pw1[i] %= M1
    pw2[i] %= M2

class Solution:
    def find(self, num, i, n, ctr, fhash, shash, tight, curr):
        if i >= n:
            if tight or ctr[0] > 0:
                return float('inf')
            for d in range(1, 10):
                if ctr[d] > 0 and ctr[d] != d:
                    return float('inf')
            return curr
        key = (i, fhash, shash, tight)
        if key in self.cache:
            return self.cache[key]
        mindigit = 0
        if tight:
            mindigit = int(num[i])
        for d in range(mindigit, 10):
            if ctr[d] == d:
                continue
            ctr[d] += 1
            cres = self.find(num, i + 1, n, ctr, (fhash + d * pw1[d]) % M1, (shash + d * pw2[d]) % M2, tight and d == mindigit, 10 * curr + d)
            if cres < float('inf'):
                self.cache[key] = cres
                return cres
            ctr[d] -= 1
        self.cache[key] = float('inf')
        return float('inf')
    
    def nextBeautifulNumber(self, n: int) -> int:
        self.cache = {}
        a = self.find(str(n), 0, len(str(n)), [0] * 10, 0, 0, True, 0)
        self.cache = {}
        b = self.find(str(10 ** len(str(n))), 0, len(str(10 ** len(str(n)))), [0] * 10, 0, 0, True, 0)
        return min(a, b)