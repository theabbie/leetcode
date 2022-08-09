class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [1] * n
        longest = [0] * 26
        for i in range(n - 1, -1, -1):
            curr = ord(s[i]) - ord('a')
            for j in range(curr - k, curr + k + 1):
                if 0 <= j < 26:
                    dp[i] = max(dp[i], 1 + longest[j])
            longest[curr] = max(longest[curr], dp[i])
        return max(dp)