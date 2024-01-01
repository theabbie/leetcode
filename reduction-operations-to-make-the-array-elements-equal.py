class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        d = set()
        res = 0
        for i in range(n):
            d.add(nums[i])
            res += len(d) - 1
        return res