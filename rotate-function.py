class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        curr = 0
        for i in range(n):
            curr += i * nums[i]
            total += nums[i]
        mval = float('-inf')
        for i in range(n - 1, -1, -1):
            curr -= n * nums[i] - total
            mval = max(mval, curr)
        return mval