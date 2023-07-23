import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    curr = 0
    arr = [0] * n
    for i in range(1, n + 1):
        if math.ceil(i / k) > curr:
            curr += 1
            arr[i - 1] = 1
    curr = 0
    for i in range(n - 1, -1, -1):
        if arr[i] == 1:
            curr += 1
        if math.ceil((n - i) / k) > curr:
            curr += 1
            arr[i] = 1
    print(arr.count(1))