t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    buckets = [[] for _ in range(k)]
    idealbuckets = [set() for _ in range(k)]
    for i in range(n):
        buckets[i % k].append(arr[i])
        idealbuckets[i % k].add(i + 1)
    err = 0
    for i in range(k):
        for j in buckets[i]:
            if j not in idealbuckets[i]:
                err += 1
    if err == 0:
        print(0)
    elif err == 2:
        print(1)
    else:
        print(-1)