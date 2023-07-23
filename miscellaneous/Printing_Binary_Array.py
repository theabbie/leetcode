t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(*[1 - el for el in arr])