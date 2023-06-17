from collections import Counter

class Solution:
    def fourSumCount(self, a, b, c, d):
        n = len(a)
        res = 0
        ctr = Counter()
        for i in range(n):
            for j in range(n):
                ctr[a[i] + b[j]] += 1
        for i in range(n):
            for j in range(n):
                res += ctr[-c[i] - d[j]]
        return res