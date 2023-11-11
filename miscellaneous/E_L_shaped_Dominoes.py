import sys

input = sys.stdin.readline

t = int(input())

good = {(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 1), (3, 2)}

for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())), list(map(int, input().split()))]
    dp = [[0] * 4 for _ in range(n + 1)]
    dp[n][1] = dp[n][2] = dp[n][3] = float('-inf')
    for i in range(n - 1, -1, -1):
        for prev in range(4):
            for curr in range(4):
                s = 0
                for k in range(2):
                    if curr & (1 << k):
                        s += arr[k][i]
                if (prev, curr) in good:
                    if prev != 0:
                        curr = 0
                    dp[i][prev] = max(dp[i][prev], s + dp[i + 1][curr])
    print(dp[0][0])