t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    found = False
    res = -1
    for i in range(n - 1):
        if s[i] == "R" and s[i + 1] == "L":
            found = True
        if s[i] == "L" and s[i + 1] == "R":
            res = i + 1
    if found:
        print(0)
    else:
        print(res)