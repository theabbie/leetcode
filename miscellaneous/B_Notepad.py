from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = False
    pos = {}
    for i in range(n - 1):
        if s[i:i+2] not in pos:
            pos[s[i:i+2]] = i + 1
        else:
            if pos[s[i:i+2]] < i:
                res = True
                break
    print("YES" if res else "NO")