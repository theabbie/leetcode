from collections import Counter

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ctr = Counter()
        p = 0
        ctr[p] += 1
        res = 0
        for el in nums:
            p += el
            res += ctr[p - goal]
            ctr[p] += 1
        return res