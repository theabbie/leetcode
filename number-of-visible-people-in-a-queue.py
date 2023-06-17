class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        prevhigher = [-1] * n
        nexthigher = [n] * n
        stack = []
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] < heights[i]:
                curr = stack.pop()
                nexthigher[curr] = i
            if len(stack) > 0:
                prevhigher[i] = stack[-1]
            stack.append(i)
        res = [0] * n
        ctr = [0] * n
        for i in range(n - 1, -1, -1):
            res[i] = ctr[i]
            if nexthigher[i] != n:
                res[i] += 1
            if prevhigher[i] != -1:
                ctr[prevhigher[i]] += 1
        return res