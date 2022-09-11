t = int(input())

for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    same = True
    for i in range(n):
        a = s1[i]
        b = s2[i]
        if a == "G":
            a = "B"
        if b == "G":
            b = "B"
        if a != b:
            same = False
            break
    if same:
        print("YES")
    else:
        print("NO")