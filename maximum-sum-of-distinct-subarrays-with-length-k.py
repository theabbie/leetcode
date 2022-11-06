from collections import Counter

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = 0
        res = 0
        ctr = Counter()
        l = 0
        for i in range(n):
            s += nums[i]
            if ctr[nums[i]] == 0:
                l += 1
            ctr[nums[i]] += 1
            if i >= k:
                s -= nums[i - k]
                ctr[nums[i - k]] -= 1
                if ctr[nums[i - k]] == 0:
                    l -= 1
            if i >= k - 1:
                if l == k:
                    res = max(res, s)
        return res