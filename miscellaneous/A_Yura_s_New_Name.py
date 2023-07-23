t = int(input())

for _ in range(t):
    s = input()
    if s == '^':
        print(1)
        continue
    n = len(s)
    res = 0
    preveye = False
    for i in range(n):
        if s[i] == '_':
            if not preveye:
                res += 1
            if i == n - 1 or s[i + 1] != '^':
                res += 1
                preveye = True
        else:
            preveye = True
    print(res)