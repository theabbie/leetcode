from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        ctr = Counter()
        res = 0
        for j in range(n + 1):
            target = p[j] - k
            res += ctr[target]
            ctr[p[j]] += 1
        return res