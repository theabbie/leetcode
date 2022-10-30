t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] > 1:
        print(0)
        continue
    l = 0
    while l < n and arr[l] == 1:
        l += 1
    if 2 * l - 2 >= n:
        print(0)
    else:
        print(arr[2 * l - 2])