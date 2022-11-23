t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    valid = True
    x = 0
    if s[0] in "Yes":
        x = "Yes".index(s[0])
    for i in range(n):
        if s[i] != "Yes"[(i + x) % 3]:
            valid = False
            break
    print("YES" if valid else "NO")