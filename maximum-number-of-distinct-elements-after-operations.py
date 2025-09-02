class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        prev = float('-inf')
        for i in range(n):
            if nums[i] <= prev:
                maxadd = min(k, prev - nums[i] + 1)
                nums[i] += maxadd
            else:
                maxsub = min(k, nums[i] - prev - 1)
                nums[i] -= maxsub
            prev = nums[i]
        return len(set(nums))