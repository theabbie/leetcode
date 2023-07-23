n = int(input())

arr = list(map(int, input().split()))

k = float('inf')

for i in range(n):
    if i > 0:
        k = min(k, min(arr[i], arr[0]) // i)
    if i < n - 1:
        k = min(k, min(arr[i], arr[-1]) // (n - i - 1))

print(k)