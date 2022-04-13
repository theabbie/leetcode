class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        valIndexes = {}
        total = 0
        for i in range(n):
            valIndexes[nums[i]] = valIndexes.get(nums[i], 0) + 1
        for val in valIndexes:
            freq = valIndexes[val]
            total += freq * (freq - 1) // 2
        return total