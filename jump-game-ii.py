class Solution:
    memo = {}
    
    def jumpRec(self, nums, i):
        if i in self.memo:
            return self.memo[i]
        if i >= len(nums) - 1:
            return 0
        minJumps = float('inf')
        curr = nums[i]
        for jump in range(1, curr + 1):
            numJumps = self.jumpRec(nums, i + jump)
            minJumps = min(minJumps, 1 + numJumps)
        self.memo[i] = minJumps
        return minJumps
    
    def jump(self, nums: List[int], i = 0) -> int:
        self.memo = {}
        return self.jumpRec(nums, 0)