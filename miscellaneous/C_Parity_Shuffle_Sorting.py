t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = []
    for i in range(n):
        if arr[i] % 2 == 0:
            smallestodd = i
            smallesteven = i
            for j in range(i):
                if arr[j] % 2 == 1:
                    if arr[j] <= arr[smallestodd]:
                        smallestodd = j
            for j in range(i + 1, n):
                if arr[j] % 2 == 0:
                    if arr[j] <= arr[smallesteven]:
                        smallesteven = j
            if arr[i] > arr[smallestodd] <= arr[smallesteven]:
                res.append((smallestodd, i))
            elif arr[i] > arr[smallesteven]:
                res.append((i, smallesteven))
        else:
            smallesteven = i
            smallestodd = i
            for j in range(i):
                if arr[j] % 2 == 0:
                    if arr[j] <= arr[smallesteven]:
                        smallesteven = j
            for j in range(i + 1, n):
                if arr[j] % 2 == 1:
                    if arr[j] <= arr[smallestodd]:
                        smallestodd = j
            if arr[i] > arr[smallesteven] <= arr[smallestodd]:
                res.append((smallesteven, i))
            elif arr[i] > arr[smallestodd]:
                res.append((i, smallestodd))
    print(len(res))
    for step in res:
        print(*step)