t = int(input())

def solve(arr):
    n = len(arr)
    o = t = 0
    for el in arr:
        if el == 1:
            o += 1
        else:
            t += 1
    currt = 0
    for i in range(n):
        if arr[i] == 2:
            currt += 1
        if 2 * currt == t:
            print(i + 1)
            return
    print(-1)

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    solve(arr)