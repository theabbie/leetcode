t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    s = input()
    if d == 0:
        print(s + "0" if s != "0" else "0")
        continue
    pos = n
    for i in range(n):
        if d > int(s[i]):
            pos = i
            break
    print(s[:pos] + str(d) + s[pos:])