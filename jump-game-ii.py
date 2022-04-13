class Solution:
    memo = {}
    
    def jumpRec(self, nums, n, i):
        if i in self.memo:
            return self.memo[i]
        if i >= n - 1:
            self.memo[i] = 0
            return 0
        minJumps = float('inf')
        curr = nums[i]
        for jump in range(1, curr + 1):
            if i + jump <= n - 1:
                numJumps = self.jumpRec(nums, n, i + jump)
                minJumps = min(minJumps, 1 + numJumps)
        self.memo[i] = minJumps
        return minJumps
    
    def jump(self, nums: List[int]) -> int:
        self.memo.clear()
        return self.jumpRec(nums, len(nums), 0)