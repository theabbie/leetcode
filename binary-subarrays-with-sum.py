class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def count(x):
            res = 0
            i = s = 0
            for j in range(len(nums)):
                s += nums[j]
                while i <= j and s > x:
                    s -= nums[i]
                    i += 1
                res += j - i + 1
            return res
        return count(goal) - count(goal - 1)