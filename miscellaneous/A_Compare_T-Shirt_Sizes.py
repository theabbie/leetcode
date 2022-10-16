t = int(input())

for _ in range(t):
    a, b = input().split()
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while i < m and a[i] == "X":
        i += 1
    while j < n and b[j] == "X":
        j += 1
    mp = { "S": 0, "M": 1, "L": 2 }
    sg = {"S": -1, "M": 1, "L": 1}
    x = (mp[a[i]], sg[a[i]] * i)
    y = (mp[b[j]], sg[b[j]] * j)
    if x < y:
        print("<")
    elif x > y:
        print(">")
    else:
        print("=")