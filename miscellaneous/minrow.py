def possible(arr, l):
    n = len(arr)
    total = 0
    for i in range(n):
        diff = 1
        if (l - total) % (i + 1) == 0:
            diff = 0
        if arr[i] > (l - total) // (i + 1) + diff:
            return False
        total += arr[i]
    return True

arr = list(map(int, input().split()))

end = sum(arr)

while not possible(arr, end):
    end *= 2

beg = end // 2

res = beg

while beg <= end:
    mid = (beg + end) // 2
    if possible(arr, mid):
        res = mid
        end = mid - 1
    else:
        beg = mid + 1

print(res, res - sum(arr))