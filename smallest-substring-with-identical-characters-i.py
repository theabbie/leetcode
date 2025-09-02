from collections import deque

def ops(s, mid, p, dp):
    n = len(s)
    dp[n][0] = dp[n][1] = 0
    q = [deque(maxlen = n + 1), deque(maxlen = n + 1)]
    for i in range(n, -1, -1):
        for val in range(2):
            while q[1 - val] and q[1 - val][-1][1] > i + mid:
                q[1 - val].pop()
            if q[1 - val]:
                dp[i][val] = q[1 - val][-1][0] - p[1 - val][i]
        for val in range(2):
            while q[val] and dp[i][val] + p[val][i] < q[val][0][0]:
                q[val].popleft()
            q[val].appendleft((dp[i][val] + p[val][i], i))
    return min(dp[0])

class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        dp = [[float('inf'), float('inf')] for _ in range(n + 1)]
        p = [[0] * (n + 1), [0] * (n + 1)]
        for i in range(n):
            p[0][i + 1] = p[0][i] + 1 - int(s[i])
            p[1][i + 1] = p[1][i] + int(s[i])
        beg = 1
        end = n
        while beg <= end:
            mid = (beg + end) // 2
            if ops(s, mid, p, dp) <= numOps:
                end = mid - 1
            else:
                beg = mid + 1
        return end + 1