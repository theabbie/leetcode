n = int(input())

arr = list(map(int, input().split()))

res = 0

ctr = 0

for i in range(n):
    if arr[i] == i + 1:
        res += ctr
        ctr += 1
    elif 1 <= arr[i] <= i and arr[arr[i] - 1] == i + 1:
        res += 1

print(res)