class Solution:
    memo = {}
    def canJump(self, nums, i=0):
        if i in self.memo:
            return self.memo[i]
        if i >= len(nums) - 1:
            self.memo[i] = True
            return True
        canJumpBool = False
        curr = nums[i]
        for jump in range(1, curr + 1):
            if self.canJump(nums, i + jump):
                canJumpBool = True
                break
        self.memo[i] = canJumpBool
        return canJumpBool

print(Solution().canJump([3,2,1,0,4]))