from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        target = len(Counter(nums))
        for i in range(n):
            ctr = Counter()
            for j in range(i, n):
                ctr[nums[j]] += 1
                if len(ctr) == target:
                    res += 1
        return res