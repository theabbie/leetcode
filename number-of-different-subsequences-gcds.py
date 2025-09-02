MX = 200000
v = [False] * (MX + 1)
f = [[] for _ in range(MX + 1)]
for i in range(1, MX + 1):
    j = 1
    while i * j <= MX:
        f[i * j].append(i)
        j += 1

class Solution:
    @cache
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        M = max(nums)
        for x in nums:
            v[x] = True
        res = 0
        cand = set()
        for el in nums:
            for c in f[el]:
                cand.add(c)
        for g in cand:
            mul = 1
            currgcd = 0
            while g * mul <= M:
                if v[g * mul]:
                    currgcd = self.gcd(currgcd, mul)
                mul += 1
            if currgcd == 1:
                res += 1
        for x in nums:
            v[x] = False
        return res