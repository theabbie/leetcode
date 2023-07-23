n = int(input())

arr = list(map(int, input().split()))

res = [0] * n

for i in range(7 * n):
    res[i // 7] += arr[i]

print(*res)