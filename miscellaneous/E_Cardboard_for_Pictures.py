t = int(input())

def area(arr, w):
    return sum((el + 2 * w) * (el + 2 * w) for el in arr)

res = []

for _ in range(t):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    end = 1
    while area(arr, end) < c:
        end *= 2
    beg = end // 2
    w = end
    while beg <= end:
        mid = (beg + end) // 2
        if area(arr, mid) <= c:
            w = mid
            beg = mid + 1
        else:
            end = mid - 1
    res.append(w)

print(*res)