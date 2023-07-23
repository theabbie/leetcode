t = int(input())

x = "codeforces"

for _ in range(t):
    s = input()
    res = 0
    for i in range(10):
        if s[i] != x[i]:
            res += 1
    print(res)