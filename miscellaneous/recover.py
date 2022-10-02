t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = [arr[0]]
    valid = True
    for i in range(1, n):
        if d[-1] >= arr[i] and arr[i] > 0:
            valid = False
            break
        d.append(d[-1] + arr[i])
    if valid:
        print(*d)
    else:
        print(-1)