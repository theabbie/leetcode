class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        next_lowest = [n for i in range(n)]
        prev_lowest = [-1 for i in range(n)]
        res = 0
        stack = []
        for i in range(n):
            while len(stack) > 0 and nums[i] < nums[stack[-1]]:
                curr = stack.pop()
                next_lowest[curr] = i
            if len(stack) > 0:
                prev_lowest[i] = stack[-1]
            stack.append(i)
        for i in range(n):
            if prev_lowest[i] < k < next_lowest[i]:
                currArea = (next_lowest[i] - prev_lowest[i] - 1) * nums[i]
                res = max(res, currArea)
        return res