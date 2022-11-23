t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0] == min(arr):
        print("Yes")
    else:
        print("No")