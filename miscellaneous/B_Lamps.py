from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    lamps = []
    for _ in range(n):
        a, b = map(int, input().split())
        lamps.append((a, b))
    lamps.sort(key = lambda p: (p[0], -p[1]))
    res = 0
    i = 0
    on = 0
    status = [0] * n
    maxon = 0
    for j in range(n):
        if lamps[j][0] <= maxon:
            continue
        on += 1
        maxon = max(maxon, on)
        status[j] = 1
        res += lamps[j][1]
        tempon = on
        while i < n and lamps[i][0] <= tempon:
            if status[i] == 1:
                status[i] = 0
                on -= 1
            i += 1
        if i >= n:
            break
    print(res)