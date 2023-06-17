from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = defaultdict(int)
        totalctr = defaultdict(int)
        for i in range(n):
            total[nums[i]] += i
            totalctr[nums[i]] += 1
        res = [0] * n
        curr = defaultdict(int)
        ctr = defaultdict(int)
        for i in range(n):
            res[i] = ctr[nums[i]] * i - curr[nums[i]] + total[nums[i]] - curr[nums[i]] - i - (totalctr[nums[i]] - ctr[nums[i]] - 1) * i
            curr[nums[i]] += i
            ctr[nums[i]] += 1
        return res