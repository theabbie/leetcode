t = int(input())

for _ in range(t):
    ctr = list(map(int, input().split()))
    if min(ctr[1:]) == 0:
        print(min(range(1, 10), key = lambda i: (ctr[i], i)))
    elif ctr[0] == 0:
        print(10)
    else:
        res = None
        for i in range(1, 10):
            if res == None:
                res = (ctr[i] + 1, str(i) * (ctr[i] + 1))
            else:
                res = min(res, (ctr[i] + 1, str(i) * (ctr[i] + 1)))
        res = min(res, (ctr[0] + 2, "1" + "0" * (ctr[0] + 1)))
        print(res[1])