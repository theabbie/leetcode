class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key = lambda a: 1 if a == 0 else 0)
        