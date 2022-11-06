n, p = map(int, input().split())

arr = list(map(int, input().split()))

def numproducts(arr, t):
    res = 0
    for el in arr:
        res += t // el
    return res

end = 1
while numproducts(arr, end) < p:
    end *= 2
beg = end // 2
res = end

while beg <= end:
    mid = (beg + end) // 2
    if numproducts(arr, mid) >= p:
        res = mid
        end = mid - 1
    else:
        beg = mid + 1

print(res)