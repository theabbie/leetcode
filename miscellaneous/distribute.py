t = int(input())


def ways(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

for _ in range(t):
    n = int(input())
    total = ways(n, n // 2)
    k = 3 * total // 5
    # 998244353 
    print(ways(n - 2, n // 3))