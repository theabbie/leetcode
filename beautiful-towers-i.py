class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        pref = [0] * n
        suff = [0] * n
        stack = []
        for i in range(n):
            while len(stack) > 0 and maxHeights[i] < maxHeights[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                pref[i] = maxHeights[i] * (i - stack[-1]) + pref[stack[-1]]
            else:
                pref[i] = maxHeights[i] * (i + 1)
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and maxHeights[i] < maxHeights[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                suff[i] = maxHeights[i] * (stack[-1] - i) + suff[stack[-1]]
            else:
                suff[i] = maxHeights[i] * (n - i)
            stack.append(i)
        res = 0
        for i in range(n):
            res = max(res, pref[i] + suff[i] - maxHeights[i])
        return res