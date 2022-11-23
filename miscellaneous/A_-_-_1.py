n, x = map(int, input().split())

arr = list(map(int, input().split()))

res = -1

for i in range(n):
    if arr[i] == x:
        res = i + 1

print(res)