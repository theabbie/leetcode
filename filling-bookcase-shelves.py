class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            s = 0
            mx = 0
            for j in range(i, n):
                s += books[j][0]
                mx = max(mx, books[j][1])
                if s > shelfWidth:
                    break
                dp[i] = min(dp[i], mx + dp[j + 1])
        return dp[0]