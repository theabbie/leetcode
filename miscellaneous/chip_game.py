t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if (n % 2 == 1) ^ (m % 2 == 1):
        print("Burenka")
    else:
        print("Tonya")