t = int(input())

for _ in range(t):
    n = int(input())
    if n & 1:
        if n == 3:
            print("NO")
        else:
            print("YES")
            print(*([n - 3, 1 - n] * ((n - 1) // 2) + [n - 3]))
    else:
        print("YES")
        print(*([1, -1] * (n // 2)))