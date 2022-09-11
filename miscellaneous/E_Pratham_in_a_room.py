t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if "1" not in s:
        print(n)
    else:
        i = s.index("1")
        i = max(i + 1, n - i)
        j = n - s[::-1].index("1") - 1
        j = max(j + 1, n - j)
        print(max(2 * i, 2 * j))