t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = arr[:]
    y = arr[:]
    for i in range(n):
        if i & 1:
            x[i] *= -1
        else:
            y[i] *= -1
    px = [0]
    py = [0]
    for i in range(n):
        px.append(px[-1] + x[i])
        py.append(py[-1] + y[i])
    print(px, py)