t = int(input())

for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))
    print(1 + max(range(n), key = lambda i: vals[i]))