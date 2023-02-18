def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = float('inf')
    for i in range(n):
        k = i + 1
        for j in range(i + 2, n):
            while k < n and 2 * arr[k] <= arr[i] + arr[j]:
                k += 1
            if k < n:
                res = min(res, abs(arr[i] + arr[j] - 2 * arr[k]))
            if k > 0:
                res = min(res, abs(arr[i] + arr[j] - 2 * arr[k - 1]))
    print(res)
    
SINGLE = False

t = 1

if not SINGLE:
    t = int(input())

for _ in range(t):
    solve()