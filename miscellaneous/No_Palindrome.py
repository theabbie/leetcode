t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    print(1 + ((n - 1) // 4) * 2 + sum([0, 0, 1, 1][:(n - 1) % 4]))