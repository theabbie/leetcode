class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = -1
        for el in set(nums):
            ctr = 0
            for i in range(n - k + 1):
                if el in nums[i:i+k]:
                    ctr += 1
            if ctr == 1:
                res = max(res, el)
        return res