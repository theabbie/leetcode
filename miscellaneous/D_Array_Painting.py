t = int(input())

def check(arr, lim):
    n = len(arr)

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    beg = 0
    end = n
    res = end
    while beg <= end:
        mid = (beg + end) // 2
        if check(arr, mid):
            res = end
            end = mid - 1
        else:
            beg = mid + 1
    print(res)