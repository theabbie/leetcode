n = int(input())

arr = list(map(int, input().split()))

arr = [0 if el < 0 else 1 for el in arr]

q = int(input())

for _ in range(q):
    k = int(input())
    ctr = [[0, 0] for _ in range(k)]
    curr = 0
    for i in range(n):
        curr += ctr[i % k][1 - arr[i]]
        ctr[i % k][arr[i]] += 1
    print(curr)