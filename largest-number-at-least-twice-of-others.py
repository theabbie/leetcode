class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        currmax = float('-inf')
        secmax = float('-inf')
        for num in nums:
            if num > currmax:
                secmax = currmax
                currmax = num
            elif num > secmax and num != currmax:
                secmax = num
        return nums.index(currmax) if currmax >= 2 * secmax else -1