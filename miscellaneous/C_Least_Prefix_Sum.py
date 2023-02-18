t = int(input())

def mininv(arr):
    p = 0
    res = 0
    for el in arr:
        if p + el >= 0:
            p += el
        else:
            res += 1
            p -= el
    return res

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(m):
        arr[i] *= -1
    print(mininv(arr[1:m][::-1]) + mininv(arr[m:]))