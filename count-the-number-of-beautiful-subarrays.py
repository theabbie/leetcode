from collections import Counter

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        p = [0] * 32
        ctr = Counter()
        ctr[tuple(p)] = 1
        res = 0
        for el in nums:
            for b in range(32):
                if el & (1 << b):
                    p[b] += 1
                    p[b] %= 2
            curr = tuple(p)
            res += ctr[curr]
            ctr[curr] += 1
        return res