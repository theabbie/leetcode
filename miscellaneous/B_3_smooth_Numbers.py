n = int(input())

x = y = 0

while n % 2 == 0:
    n //= 2
    x += 1

while n % 3 == 0:
    n //= 3
    y += 1

print("Yes" if n == 1 else "No")