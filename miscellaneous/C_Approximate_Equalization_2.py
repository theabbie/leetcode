n = int(input())

arr = list(map(int, input().split()))

s = sum(arr)

k = s // n

arr.sort()

x = (k + 1) * n - s

res = 0

for i in range(x):
    res += abs(arr[i] - k)

for i in range(x, n):
    res += abs(arr[i] - k - 1)

print(res // 2)