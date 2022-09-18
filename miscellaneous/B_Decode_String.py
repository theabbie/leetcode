t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    p = 0
    res = []
    done = [False] * n
    i = 0
    while i < n:
        if s[i] == '0':
            while i < n and s[i] == '0':
                i += 1
            i -= 1
            done[i] = done[i - 1] = done[i - 2] = True
        i += 1
    i = 0
    while i < n:
        if done[i]:
            res.append(chr(ord('a') + int(s[i:i+2]) - 1))
            i += 2
        else:
            res.append(chr(ord('a') + int(s[i]) - 1))
        i += 1
    print("".join(res))