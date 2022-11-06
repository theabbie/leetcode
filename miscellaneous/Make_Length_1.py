t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if n == 1:
        print("YES")
        continue
    ctr = 0
    pos = True
    for i, c in enumerate(s):
        if c == "1":
            ctr += 1
        if c == "0" or i == n - 1:
            if ctr & 1:
                pos = False
                break
    print("YES" if pos else "NO")