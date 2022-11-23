t = int(input())

for _ in range(t):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    print(b % x - a % x)