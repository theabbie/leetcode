from collections import Counter

M = 1000000007

class Solution:
    def countPairs(self, arr: List[int]) -> int:
        arr.sort()
        pw = 1
        res = 0
        while pw <= 2 * arr[-1]:
            ctr = Counter()
            for el in arr:
                res += ctr[pw - el]
                ctr[el] += 1
            pw *= 2
        return res % M