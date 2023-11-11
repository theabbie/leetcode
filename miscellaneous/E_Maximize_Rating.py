import math

n = int(input())

arr = list(map(int, input().split()))

arr.reverse()

dp = [[-1200] * (n + 1) for _ in range(n + 1)]

dp[0][0] = 0

bsum = [0] * (n + 1)
bpow = [1] * (n + 1)

PRECISION = 100000000000000

for i in range(n):
    bsum[i + 1] = bsum[i] + bpow[i]
    bpow[i + 1] = 0.9 * bpow[i]
    bsum[i + 1] = round(PRECISION * bsum[i + 1]) / PRECISION
    bpow[i + 1] = round(PRECISION * bpow[i + 1]) / PRECISION

sqrt = [1200/math.sqrt(i) if i > 0 else 0 for i in range(n + 1)]

for i in range(1, n + 1):
    sqrt[i] = round(PRECISION * sqrt[i]) / PRECISION

for i in range(1, n + 1):
    for pick in range(1, n + 1):
        old = dp[i - 1][pick - 1]
        if pick > 1:
            old += sqrt[pick - 1]
        old *= bsum[pick - 1]
        dp[i][pick] = max(dp[i - 1][pick], (bpow[pick - 1] * arr[i - 1] + old)/bsum[pick] - sqrt[pick])

print(round(PRECISION * max(dp[n])) / PRECISION)