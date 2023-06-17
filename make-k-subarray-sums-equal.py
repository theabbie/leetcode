from collections import Counter

class Solution:
    def GCD(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        k = self.GCD(len(arr), k)
        ctr = [[] for _ in range(k)]
        median = [0] * k
        for i in range(len(arr)):
            ctr[i % k].append(arr[i])
        for i in range(k):
            n = len(ctr[i])
            ctr[i].sort()
            median[i] = ctr[i][(n - 1) // 2]
        res = 0
        for i in range(k):
            n = len(ctr[i])
            for j in range(n):
                res += abs(ctr[i][j] - median[i])
        return res