class Solution:
    def getSum(self, nums, n, cmp):
        stack = []
        nextpos = [n] * n
        prevpos = [-1] * n
        for i in range(n):
            while len(stack) > 0 and cmp(nums[i], nums[stack[-1]]):
                curr = stack.pop()
                nextpos[curr] = i
            if len(stack) > 0:
                prevpos[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(n):
            l = prevpos[i]
            r = nextpos[i]
            res += (i - l) * (r - i) * nums[i]
        return res
    
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        maxvals = self.getSum(nums, n, lambda a, b: a > b)
        minvals = self.getSum(nums, n, lambda a, b: a < b)
        return maxvals - minvals