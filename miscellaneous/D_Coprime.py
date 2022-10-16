t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = -1
    pos = {}
    for i in range(n):
        pos[arr[i]] = i
    for i in pos:
        for j in pos:
            if pos[i] + pos[j] + 2 > res and gcd(i, j) == 1:
                res = max(res, pos[i] + pos[j] + 2)
    print(res)