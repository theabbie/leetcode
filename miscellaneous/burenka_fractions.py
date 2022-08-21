t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    m = a * d
    n = b * c
    if m == 0 or n == 0:
        if m == 0 and n == 0:
            print(0)
        else:
            print(1)
        continue
    if m == n:
        print(0)
    elif m % n == 0 or n % m == 0:
        print(1)
    else:
        print(2)