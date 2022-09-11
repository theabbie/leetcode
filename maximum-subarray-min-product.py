class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        p = [0]
        for i in range(n):
            while len(stack) > 0 and nums[i] < nums[stack[-1]]:
                curr = stack.pop()
                next_smaller[curr] = i
            if len(stack) > 0:
                prev_smaller[i] = stack[-1]
            stack.append(i)
            p.append(p[-1] + nums[i])
        res = float('-inf')
        for i in range(n):
            l = prev_smaller[i]
            r = next_smaller[i]
            res = max(res, nums[i] * (p[r] - p[l + 1]))
        return res % (10 ** 9 + 7)