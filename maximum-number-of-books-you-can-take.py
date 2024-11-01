class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        prv = [-1] * n
        stack = []
        for i in range(n):
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()
            if stack:
                prv[i] = stack[-1]
            stack.append(i)
        dp = [0] * n
        for i in range(n):
            if prv[i] != -1:
                dp[i] = dp[prv[i]]
            l = min(i - prv[i], books[i])
            dp[i] += books[i] * l - l * (l - 1) // 2
        return max(dp)