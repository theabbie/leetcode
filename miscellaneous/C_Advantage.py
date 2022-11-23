t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    order = sorted(arr)
    mp = {}
    for i in range(n):
        if i < n - 1:
            mp[order[i]] = order[-1]
        else:
            mp[order[i]] = order[-2]
    print(*[el - mp[el] for el in arr])