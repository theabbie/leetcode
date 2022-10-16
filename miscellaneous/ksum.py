def solve(N, K, S, arr):
    sums = [[0, 0] for _ in range(K)]
    for i in range(N):
        sums[i % K][0] += arr[i]
        sums[i % K][1] += 1
    res = 0
    for i in range(K):
        if sums[i][0] <= S:
            res = max(res, sums[i][1])
    return res

print(solve(4, 3, 6, [1,2,3,4]))