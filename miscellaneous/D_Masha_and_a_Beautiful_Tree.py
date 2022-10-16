t = int(input())

def sort(arr, i, j):
    if i + 1 >= j:
        ctr = 0
        if arr[i] > arr[j]:
            ctr = 1
        valid = True
        if abs(arr[i] - arr[j]) > 1:
            valid = False
        return (min(arr[i], arr[j]), max(arr[i], arr[j]), ctr, valid)
    mid = (i + j) // 2
    ctr = 0
    lmin, lmax, x, lvalid = sort(arr, i, mid)
    rmin, rmax, y, rvalid = sort(arr, mid + 1, j)
    cmin = min(lmin, rmin)
    cmax = max(lmax, rmax)
    valid = lvalid and rvalid
    if cmax - cmin != j - i:
        valid = False
    if lmin > rmin:
        ctr += 1
    return (cmin, cmax, x + y + ctr, valid)

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    amin, amax, res, valid = sort(arr, 0, n - 1)
    if not valid:
        print(-1)
    else:
        print(res)