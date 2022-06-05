class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n = len(nums)
        pos = {}
        for i in range(n):
            pos[nums[i]] = i
        for a, b in operations:
            i = pos[a]
            nums[i] = b
            pos[b] = i
        return nums