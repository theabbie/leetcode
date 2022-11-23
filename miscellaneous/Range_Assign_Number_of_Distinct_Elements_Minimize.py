t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n <= 2:
        print("YES")
        continue
    if arr[0] == arr[-1]:
        print("YES")
    else:
        found = False
        for i in range(n - 1):
            if arr[i] == arr[0] and arr[i + 1] == arr[-1]:
                found = True
                break
        print("YES" if found else "NO")