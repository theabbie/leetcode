t = int(input())

M = 10 ** 9 + 7

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n):
        p[i] -= 1
    arr = list(map(int, input().split()))
    ctr = arr.count(0)
    acp = [i for i in range(n)]
    for i in range(n):
        acp[i] = acp[p[i]]
    acp = set(acp)
    prev = None
    valid = True
    contains = False
    val = None
    ctrctr = 0
    for i in acp:
        if arr[i] != 0:
            ctrctr += 1
            val = arr[i]
            if prev == None:
                prev = arr[i]
            if arr[i] != prev:
                valid = False
                break
        else:
            contains = True
    if not valid:
        print(0)
        continue
    ctr = 0
    for i in range(n):
        if i not in acp:
            if arr[i] == 0:
                ctr += 1
            elif arr[i] != val and ctrctr != 0:
                valid = False
    if not valid:
        print(0)
        continue
    print(pow(m, ctr + (1 if contains else 0), M))