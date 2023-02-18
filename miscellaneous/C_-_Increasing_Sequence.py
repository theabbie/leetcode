n = int(input())

arr = list(map(int, input().split()))

if arr[-1] == -1:
    for i in range(n):
        arr[i] *= -1

if n == 1:
    print("Yes")
    print(0)
    exit(0)

res = list(range(1, n + 1))

s = sum(res)
x = 0

for i in range(n):
    if arr[i] == -1:
        x += res[i]

if 2 * x >= s:
    res[-1] += 2 * x - s
elif arr[0] == 1:
    res[0] -= s - 2 * x

check = 0
valid = True

for i in range(n):
    if i < n - 1 and res[i] >= res[i + 1]:
        valid = False
    check += res[i] * arr[i]

if check == 0 and valid:
    print("Yes")
    print(*res)
else:
    print("No")