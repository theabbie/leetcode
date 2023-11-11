class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        score = nums[0]
        for el in nums:
            score &= el
        if score != 0:
            return 1
        res = 0
        curr = nums[0]
        for i in range(n):
            curr &= nums[i]
            if curr == score:
                res += 1
                if i < n - 1:
                    curr = nums[i + 1]
        return res