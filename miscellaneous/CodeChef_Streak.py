t = int(input())

def maxstreak(arr, n):
    res = 0
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and not ((arr[i] == 0) ^ (arr[i + 1] == 0)):
            ctr += 1
            i += 1
        if arr[i] != 0:
            res = max(res, ctr)
        i += 1
    return res

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    astreak = maxstreak(a, n)
    bstreak = maxstreak(b, n)
    if astreak == bstreak:
        print("Draw")
    elif astreak > bstreak:
        print("Om")
    else:
        print("Addy")