t = int(input())

M = 10 ** 9 + 7

factorial = []
factorialinv = []
pw = []

class Number:
    def factorial(N):
        factorial.extend([1] * (N + 1))
        factorialinv.extend([1] * (N + 1))
        for i in range(1, N + 1):
            factorial[i] = i * factorial[i - 1]
            factorial[i] %= M
        factorialinv[N] = pow(factorial[N], M - 2, M)
        for i in range(N - 1, -1, -1):
            factorialinv[i] = (i + 1) * factorialinv[i + 1]
            factorialinv[i] %= M

    def pw2(N):
        pw.extend([1] * (N + 1))
        for i in range(1, N + 1):
            pw[i] = 2 * pw[i - 1]
            pw[i] %= M
    
    def comb(N, K):
        return (factorial[N] * factorialinv[K] * factorialinv[N - K]) % M
    
Number.factorial(10 ** 5)
Number.pw2(10 ** 5)

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = 0
    for i in range(n):
        if arr[i] - 1 <= i:
            res += Number.comb(i, arr[i] - 1) * pw[n - i - 1]
            res %= M
    print(res)