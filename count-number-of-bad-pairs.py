from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = defaultdict(int)
        for i in range(n):
            ctr[nums[i] - i] += 1
        res = n * (n - 1) // 2
        for val in ctr.values():
            res -= val * (val - 1) // 2
        return res