t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arrset = set(arr)
    res = -1
    for i in range(n):
        g = 0
        for j in range(n):
            if arr[i] != 0:
                g = gcd(g, abs(arr[j] % arr[i]))
            if g in arrset:
                res = g
                break
            if -g in arrset:
                res = -g
                break
    print(res)