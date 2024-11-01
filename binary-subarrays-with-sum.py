class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        def count(x):
            res = 0
            i = 0
            s = 0
            for j in range(n):
                s += nums[j]
                while i <= j and s > x:
                    s -= nums[i]
                    i += 1
                res += j - i
            return res
        return count(goal) - count(goal - 1)