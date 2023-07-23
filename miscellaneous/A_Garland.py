t = int(input())

for _ in range(t):
    s = input()
    k = len(set(s))
    if k == 4:
        print(4)
    elif k == 1:
        print(-1)
    elif k == 3:
        print(4)
    else:
        s = sorted(s)
        if s[0] == s[1] and s[2] == s[3]:
            print(4)
        else:
            print(6)