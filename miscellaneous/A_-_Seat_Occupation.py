n, l = map(int, input().split())

arr = list(map(int, input().split()))

pos = True

total = 0

for i in range(n):
    diff = 1
    if (l - total) % (i + 1) == 0:
        diff = 0
    if arr[i] > (l - total) // (i + 1) + diff:
        pos = False
    total += arr[i]

print("Yes" if pos else "No")