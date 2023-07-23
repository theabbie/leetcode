t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = 0
    i = -1
    valid = True
    for j in range(n):
        if s[j] == ":":
            if i != -1 and valid and j - i > 1:
                res += 1
            i = j
            valid = True
        elif s[j] == "(":
            valid = False
    print(res)