from audioop import mul


def multiply(a, b):
    n = len(a)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += res[i][k] + res[k][j]
    return res

def pow(a, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    k = n % 2
    res = pow(a, (n - k) // 2)
    for _ in range(k):
        res = multiply(res, a)
    return res

print(pow([[1, 1], [0, 1]], 5))