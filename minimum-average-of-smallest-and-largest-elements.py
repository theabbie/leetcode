class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res = []
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            res.append((nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        return min(res)