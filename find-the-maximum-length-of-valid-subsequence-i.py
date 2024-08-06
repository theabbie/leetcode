class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = max(len([el for el in nums if el % 2 == 0]), len([el for el in nums if el % 2 == 1]))
        odd = even = 0
        for i in range(n):
            curr = 0
            if nums[i] % 2 == 0:
                curr = max(curr, 1 + odd)
                even = max(even, curr)
            else:
                curr = max(curr, 1 + even)
                odd = max(odd, curr)
            res = max(res, curr)
        return res