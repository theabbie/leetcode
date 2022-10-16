t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    z = 0
    o = 0
    for c in s:
        if c == "0":
            z += 1
        else:
            o += 1
    if z % 2 == 0 or o % 2 == 0:
        print("YES")
    else:
        print("NO")