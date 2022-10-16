t = int(input())

def numpaths(p, q):
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    return dp[q - 1]

def bcoff(n, k):
    C = [0 for i in range(k+1)]
    C[0] = 1
    for i in range(1, n + 1):
        j = min(i, k)
        while (j > 0):
            C[j] = C[j] + C[j-1]
            j -= 1
    return C[k]

for _ in range(t):
    n, m = map(int, input().split())
    k = n + m - 1
    if k % 2 == 1:
        print(0)
    else:
        l = numpaths(n, m)
        m = bcoff(k, k // 2)
        print((l * m * (1 << max(k - 2, 0))) % 998244353)