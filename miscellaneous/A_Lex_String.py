t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    a = sorted(input())
    b = sorted(input())
    res = []
    i = 0
    j = 0
    lastA = False
    lastB = False
    actr = 0
    bctr = 0
    while i < n and j < m:
        if a[i] < b[j] and actr < k:
            res.append(a[i])
            if lastA:
                actr += 1
            else:
                actr = 1
            lastA = True
            lastB = False
            bctr = 0
            i += 1
        elif bctr < k:
            res.append(b[j])
            if lastB:
                bctr += 1
            else:
                bctr = 1
            lastB = True
            lastA = False
            actr = 0
            j += 1
        else:
            break
    print("".join(res))