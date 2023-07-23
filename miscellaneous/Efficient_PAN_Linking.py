t = int(input())

for _ in range(t):
    s = input()
    res = 0
    for c in s:
        res = 10 * res + int(c)
        res %= 20
    print(res)