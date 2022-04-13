class Solution: 
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        leftmost = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= leftmost:
                leftmost = i
        return leftmost == 0