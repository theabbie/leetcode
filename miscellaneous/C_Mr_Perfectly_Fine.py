t = int(input())

for _ in range(t):
    n = int(input())
    mins = {"00": float('inf'), "01": float('inf'), "10": float('inf'), "11": float('inf')}
    for _ in range(n):
        x, p = input().split()
        mins[p] = min(mins[p], int(x))
    res = min(mins["11"], mins["01"] + mins["10"])
    if res == float('inf'):
        res = -1
    print(res)