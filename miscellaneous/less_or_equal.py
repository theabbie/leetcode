n, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

if arr.count(arr[k - 1]) == 1:
    print(arr[k - 1])
else:
    print(-1)