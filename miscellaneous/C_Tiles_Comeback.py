t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if arr[0] == arr[-1] and arr.count(arr[0]) >= k:
        print("YES")
        continue
    ctr = 0
    f = n
    for i in range(n):
        if arr[i] == arr[0]:
            ctr += 1
        if ctr == k:
            f = i
            break
    l = 0
    ctr = 0
    for i in range(n - 1, -1, -1):
        if arr[i] == arr[-1]:
            ctr += 1
        if ctr == k:
            l = i
            break
    print("YES" if f < l else "NO")