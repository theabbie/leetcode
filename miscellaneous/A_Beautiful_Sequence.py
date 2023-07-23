t = int(input())

def check(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] <= i + 1:
            return "YES"
    return "NO"

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(check(arr))