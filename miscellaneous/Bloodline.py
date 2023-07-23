t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    tina = True
    while n > 0:
        curr = n % k
        if curr > 0:
            tina = not tina
        n //= k
    print("Shivansh" if not tina else "Tina")