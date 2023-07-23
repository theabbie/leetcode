t = int(input())

for _ in range(t):
    s = input()
    if s.startswith("0"):
        print(0)
        continue
    n = len(s)
    res = 1
    for i in range(n):
        if s[i] == '?':
            if i == 0:
                res *= 9
            else:
                res *= 10
    print(res)