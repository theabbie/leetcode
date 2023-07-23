t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = []
    curr = []
    breaks = 0
    for el in arr:
        if len(curr) == 0 or (curr[-1] <= el and breaks == 0):
            res.append("1")
            curr.append(el)
            continue
        if len(curr) == 0 or (curr[-1] <= el and el <= curr[0] and breaks == 1):
            res.append("1")
            curr.append(el)
            continue
        if curr[-1] > el and curr[0] >= el and breaks == 0:
            breaks += 1
            res.append("1")
            curr.append(el)
            continue
        res.append("0")
    print("".join(res))