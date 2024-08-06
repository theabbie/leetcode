class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        M = 1000000007
        n = len(arr)
        nxt = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                nxt[stack.pop()] = i
            stack.append(i)
        dp = [0] * (n + 1)
        res = 0
        for i in range(n - 1, -1, -1):
            dp[i] = (nxt[i] - i) * arr[i] + dp[nxt[i]]
            dp[i] %= M
            res += dp[i]
            res %= M
        return res