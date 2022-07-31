class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set([num for num in nums if num != 0]))