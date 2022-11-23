t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print("YES")
        continue
    vals = []
    i = 0
    while i < n:
        while i < n - 1 and arr[i] == arr[i +1]:
            i += 1
        vals.append(arr[i])
        i += 1
    exists = 0
    m = len(vals)
    if m == 1:
        print("YES")
        continue
    for i in range(m):
        if i == 0 and vals[i] < vals[i + 1]:
            exists += 1
        if i == m - 1 and vals[i - 1] > vals[i]:
            exists += 1
        if 0 < i < m - 1 and vals[i - 1] > vals[i] and vals[i + 1] > vals[i]:
            exists += 1
    print("YES" if exists == 1 else "NO")