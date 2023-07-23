t = int(input())

def check(arr, k):
    n = len(arr)
    ctr = 0
    i = 0
    for j in range(n):
        if arr[j] - arr[i] > 2 * k:
            ctr += 1
            i = j
    return ctr <= 2

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    beg = 0
    end = max(arr) - min(arr)
    res = end
    while beg <= end:
        mid = (beg + end) // 2
        if check(arr, mid):
            res = mid
            end = mid - 1
        else:
            beg = mid + 1
    print(res)