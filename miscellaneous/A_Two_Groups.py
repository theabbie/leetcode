t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = min(arr, key = abs)
    print(max(abs(sum(arr) - k) - abs(k), abs(sum(arr))))