t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    beg = min(s)
    x = 0
    for i in range(1, n):
        if s[i] == beg:
            if i < n - 1 and s[i] > s[i + 1]:
                x = i
                break
            x = i
    print(s[x] + s[:x] + s[x+1:])