n = int(input())

arr = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    arr[i] -= arr[i - 1]

print(*arr)