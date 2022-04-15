class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        currxor = 0
        allxor = n
        for i in range(n):
            currxor ^= nums[i]
            allxor ^= i
        return currxor ^ allxor