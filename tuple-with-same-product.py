from collections import Counter

class Solution:
    def tupleSameProduct(self, nums) -> int:
        n = len(nums)
        ctr = Counter()
        for i in range(n):
            for j in range(i + 1, n):
                ctr[nums[i] * nums[j]] += 1
        res = 0
        for p in ctr:
            res += 4 * ctr[p] * (ctr[p] - 1)
        return res