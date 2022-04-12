class Solution:
    memo = {}
    
    def jump(self, nums, i = 0):
        if i in self.memo:
            return self.memo[i]
        if i >= len(nums) - 1:
            return 0
        minJumps = float('inf')
        curr = nums[i]
        for jump in range(1, curr + 1):
            numJumps = self.jump(nums, i + jump)
            minJumps = min(minJumps, 1 + numJumps)
        self.memo[i] = minJumps
        return minJumps

print(Solution().jump([0]))