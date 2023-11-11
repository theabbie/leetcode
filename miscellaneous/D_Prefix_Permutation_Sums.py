t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = False
    if arr[-1] != n * (n + 1) // 2:
        arr.append(n * (n + 1) // 2)
        if sorted([arr[0]] + [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]) == list(range(1, n + 1)):
            pos = True
        print("YES" if pos else "NO")
        continue
    diff = [arr[0]] + [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    idset = set(range(1, n + 1))
    for el in diff:
        if el in idset:
            idset.remove(el)
    if len(idset) == 2 and (sum(idset) > n or diff.count(sum(idset)) == 2):
        pos = True
    idset = set(range(1, n + 1))
    if arr[-1] == n * (n + 1) // 2:
        for el in diff:
            if el in idset:
                idset.remove(el)
        if len(idset) == 1:
            x = min(idset)
            arr.insert(0, x)
            if sorted([arr[0]] + [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]) == list(range(1, n + 1)):
                pos = True
    print("YES" if pos else "NO")