t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    curr = arr[0] 
    for i in range(1, n):
        if arr[i] > arr[i-1]: 
            curr += arr[i] - arr[i-1]
    if curr == max(arr):
        print("YES")
    else:
        print("NO")