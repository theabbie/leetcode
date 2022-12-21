t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    steps = []
    for i in range(n):
        l = len("{:b}".format(arr[i]))
        old = arr[i]
        if (1 << l) >= arr[i]:
            arr[i] = 1 << l
        else:
            arr[i] = 1 << l + 1
        if arr[i] > old:
            steps.append((i + 1, arr[i] - old))
    print(len(steps))
    for i, x in steps:
        print(i, x)