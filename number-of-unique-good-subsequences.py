class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        M = 10 ** 9 + 7
        n = len(binary)
        dp = [1] * (n + 1)
        prev = {}
        zerozero = False
        zeroone = False
        for i in range(1, n + 1):
            dp[i] = 2 * dp[i - 1]
            if binary[i - 1] in prev:
                dp[i] -= dp[prev[binary[i - 1]]]
            if "0" in prev:
                if binary[i - 1] == "0" and not zerozero:
                    dp[i] -= 1
                    zerozero = True
                if binary[i - 1] == "1" and not zeroone:
                    dp[i] -= 1
                    zeroone = True
            dp[i] %= M
            prev[binary[i - 1]] = i - 1
        dp[n] = (M + dp[n] - 1) % M
        return dp[n]