t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maxyet = float('-inf')
    res = None
    for i in range(n):
        if maxyet != float('-inf') and arr[i] > maxyet:
            res = i
            break
        maxyet = max(maxyet, arr[i])
    if res == None:
        print(-1)
        continue
    print(res)
    print(*arr[:res])
    print(n - res)
    print(*arr[res:])