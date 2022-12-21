t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if len(set(s)) == 1:
        print(-1)
        continue
    res = []
    a = s.count('0')
    b = s.count('1')
    k = n
    if a >= b:
        res = []
        for i in range(2 * n):
            if s[i] == '0' and k > 0:
                k -= 1
                res.append(i + 1)
    else:
        res = []
        for i in range(2 * n):
            if s[i] == '1' and k > 0:
                k -= 1
                res.append(i + 1)
    print(*res)