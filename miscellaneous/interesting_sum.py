t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-1] + arr[-2] - arr[0] - arr[1])