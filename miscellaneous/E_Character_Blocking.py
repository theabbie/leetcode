from collections import defaultdict

t = int(input())

for _ in range(t):
    a = list(input())
    b = list(input())
    n = len(a)
    t, q = map(int, input().split())
    res = []
    eq = [1] * n
    s = n
    for i in range(n):
        if a[i] != b[i]:
            eq[i] = 0
            s -= 1
    active = n
    currt = 1
    blocks = defaultdict(set)
    for qq in range(q):
        cmd = list(map(int, input().split()))
        for i in blocks[currt]:
            old = eq[i]
            eq[i] = int(a[i] == b[i])
            s += eq[i] - old
            active += 1
        if cmd[0] == 1:
            i = cmd[1] - 1
            blocks[currt + t].add(i)
            old = eq[i]
            eq[i] = 0
            s += eq[i] - old
            active -= 1
        if cmd[0] == 2:
            x, i, y, j = cmd[1:]
            i -= 1
            j -= 1
            if x != y:
                if x == 2:
                    i, j = j, i
                a[i], b[j] = b[j], a[i]
            elif x == 1:
                a[i], a[j] = a[j], a[i]
            else:
                b[i], b[j] = b[j], b[i]
            old = eq[i]
            eq[i] = int(a[i] == b[i])
            s += eq[i] - old
            old = eq[j]
            eq[j] = int(a[j] == b[j])
            s += eq[j] - old
        if cmd[0] == 3:
            if s == active:
                res.append("YES")
            else:
                res.append("NO")
        currt += 1
    print("\n".join(res))