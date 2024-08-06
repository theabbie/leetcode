from collections import Counter

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] ^ arr[i]
        res = 0
        s = Counter()
        ctr = Counter()
        for i in range(n + 1):
            res += i * ctr[p[i]] - s[p[i]]
            ctr[p[i]] += 1
            s[p[i]] += i + 1
        return res