class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        for i in range(n):
            nums.remove(i)
        return nums