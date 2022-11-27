class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        vals = set()
        nums.sort()
        i = 0
        j = n - 1
        while i < j:
            vals.add(nums[i] + nums[j])
            i += 1
            j -= 1
        return len(vals)