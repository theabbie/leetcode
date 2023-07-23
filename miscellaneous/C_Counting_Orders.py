t = int(input())

M = 10 ** 9 + 7

N = 10 ** 5

facts = [1] * (N + 1)

for i in range(1, 21):
    facts[i] = i * facts[i - 1]
    facts[i] %= M

def larger(arr, val):
    beg = 0
    end = len(arr) - 1
    res = len(arr)
    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] > val:
            res = mid
            end = mid - 1
        else:
            beg = mid + 1
    return res

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    largevals = {}
    for el in b:
        largevals[el] = n - larger(a, el)
    res = 1
    used = 0
    for i in range(n - 1, -1, -1):
        if largevals[b[i]] == 0:
            res *= 0
            break
        res *= (largevals[b[i]] - used)
        used += 1
        res %= M
    print(res)