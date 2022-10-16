t  = int(input())

for _ in range(t):
    n = int(input())
    arr = set(map(int, input().split()))
    if n == len(arr):
        print("YES")
    else:
        print("NO")