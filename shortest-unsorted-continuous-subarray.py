class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = float('inf')
        j = float('-inf')
        sortednums = sorted(nums)
        for x in range(n):
            if sortednums[x] != nums[x]:
                i = min(i, x)
                j = max(j, x)
        return max(j - i + 1, 0)