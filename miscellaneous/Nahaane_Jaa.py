t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    valid = True
    if k not in arr:
        valid = False
    if arr.count(k) == 1 and arr[-1] == k and len(arr) > 1:
        valid = False
    print("Yes" if valid else "No")