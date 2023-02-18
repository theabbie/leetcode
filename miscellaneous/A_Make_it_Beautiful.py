t = int(input())

def check(arr):
    n = len(arr)
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + arr[i]
    for i in range(n):
        if p[i] == arr[i]:
            return False
    return True

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr[1:] = arr[1:][::-1]
    if check(arr):
        print("YES")
        print(*arr)
    else:
        print("NO")