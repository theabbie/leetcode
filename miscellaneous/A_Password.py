t = int(input())

for _ in range(t):
    n = int(input())
    unused = set(map(int, input().split()))
    used = set([i for i in range(10) if i not in unused])
    k = len(used)
    print(k * (k - 1) * 3)