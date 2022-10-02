t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(min(2, n), min(2, m))