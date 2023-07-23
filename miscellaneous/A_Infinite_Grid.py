import math

t = int(input())

for _ in range(t):
    n = int(input())
    x = int(math.sqrt(n))
    print(int(2 * (x + math.ceil(n / x))))