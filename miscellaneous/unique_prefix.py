t = int(input())

res = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    seen = set()
    i = n - 1
    while i >= 0:
        if arr[i] not in seen:
            seen.add(arr[i])
            i -= 1
        else:
            break
    print(i + 1)