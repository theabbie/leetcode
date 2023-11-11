m, n = map(int, input().split())

sell = list(map(int, input().split()))

buy = list(map(int, input().split()))

buy.sort()

sell.sort()

def buyers(x):
    beg = 0
    end = n - 1
    res = 0
    while beg <= end:
        mid = (beg + end) // 2
        if buy[mid] < x:
            res = mid + 1
            beg = mid + 1
        else:
            end = mid - 1
    return n - res

def sellers(x):
    beg = 0
    end = m - 1
    res = 0
    while beg <= end:
        mid = (beg + end) // 2
        if sell[mid] <= x:
            res = mid + 1
            beg = mid + 1
        else:
            end = mid - 1
    return res

gres = float('inf')

vals = {0}

for el in sell + buy:
    vals.add(el)
    vals.add(el + 1)
    if el > 0:
        vals.add(el - 1)

for x in vals:
    if sellers(x) >= buyers(x):
        gres = min(gres, x)

print(gres)