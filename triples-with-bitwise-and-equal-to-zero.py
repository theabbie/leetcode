from collections import defaultdict

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = defaultdict(int)
        for i in range(n):
            for j in range(n):
                ctr[nums[i] & nums[j]] += 1
        res = 0
        for i in range(n):
            for val in ctr:
                if nums[i] & val == 0:
                    res += ctr[val]
        return res