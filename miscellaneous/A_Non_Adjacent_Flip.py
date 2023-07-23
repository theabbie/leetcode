t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    x = s.count("1")
    if x & 1:
        print(-1)
    else:
        pos = []
        for i in range(n):
            if s[i] == "1":
                pos.append(i)
        m = len(pos)