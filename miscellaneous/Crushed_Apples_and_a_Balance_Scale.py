t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    if m < n:
        print("NO")
        continue
    while m % 2 == 0 and m > 0:
        m //= 2
    print("YES" if n % m == 0 else "NO")