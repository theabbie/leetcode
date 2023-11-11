from collections import Counter

def binary_search_sqrt(n):
    if n == 0 or n == 1:
        return n
    
    low, high = 1, n
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            low = mid + 1
            result = mid
        else:
            high = mid - 1
    
    return result

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = Counter(arr)
    q = int(input())
    res = []
    for _ in range(q):
        p, q = map(int, input().split())
        d = p * p - 4 * q
        sqd = binary_search_sqrt(d)
        if sqd * sqd != d:
            res.append(0)
            continue
        curr = 1
        if d == 0:
            if p & 1:
                res.append(0)
                continue
            res.append(ctr[p // 2] * (ctr[p // 2] - 1) // 2)
            continue
        for v in [p + sqd, p - sqd]:
            if v & 1:
                continue
            v //= 2
            curr *= ctr[v]
        res.append(curr)
    print(*res)