t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    a = 0
    valid = True
    for i in range(n - 1, -1, -1):
        if s[i] == "A":
            a += 1
        else:
            if a == 0:
                valid = False
                break
            a -= 1
    if valid:
        print("Yes")
    else:
        print("No")