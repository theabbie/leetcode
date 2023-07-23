import random

t = int(input())

def score(arr, k):
    p = 0
    for el in arr:
        p += el
        if p - el >= k and p < k:
            p = k
    return p

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + arr[i]
    p = list(set(p))
    random.shuffle(p)
    res = (score(arr, 0), 0)
    ctr = 0
    for el in p:
        oldres = res
        res = max(res, (score(arr, el), el))
        if res == oldres:
            ctr += 1
        if ctr * ctr >= n + 10:
            break
    print(res[1])