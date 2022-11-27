t  = int(input())

for _ in range(t):
    n = int(input())
    for a in range(1, 101):
        for b in range(a + n - 1, 101):
            if (n - 1) * a + b <= (b - a) * (b - a) <= a + (n - 1) * b:
                print(a, b)
    print()