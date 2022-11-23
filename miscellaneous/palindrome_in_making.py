t = int(input())


def minops(A):
    res = pre = 0
    for a in A:
        res += max(a - pre, 0)
        pre = a
    return res

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    j = n - 1
    res = 0
    ctr = [0] * n
    while i < j:
        if arr[i] < arr[j]:
            ctr[i] = arr[j] - arr[i]
        elif arr[i] > arr[j]:
            ctr[j] = arr[i] - arr[j]
        i += 1
        j -= 1
    print(minops(ctr))