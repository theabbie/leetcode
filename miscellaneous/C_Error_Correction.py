n, t = input().split()

n = int(n)

res = []

for val in range(n):
    s = input()
    if abs(len(s) - len(t)) > 1:
        continue
    if len(s) != len(t):
        pref = suff = 0
        while pref < min(len(s), len(t)) and s[pref] == t[pref]:
            pref += 1
        while suff < min(len(s), len(t)) and s[len(s) - suff - 1] == t[len(t) - suff - 1]:
            suff += 1
        if len(s) > len(t):
            pos = False
            for i in range(len(s)):
                if pref >= i and suff >= len(s) - i - 1:
                    pos = True
                    break
            if not pos:
                continue
        elif len(s) < len(t):
            pos = False
            for i in range(len(t)):
                if pref >= i and suff >= len(t) - i - 1:
                    pos = True
                    break
            if not pos:
                continue
    else:
        diff = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                diff += 1
        if diff > 1:
            continue
    res.append(val + 1)

print(len(res))

if len(res) > 0:
    print(*res)