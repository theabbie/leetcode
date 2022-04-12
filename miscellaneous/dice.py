import bisect
t = int(input())

for tt in range(t):
    n = int(input())
    dices = [int(x) for x in input().split()]
    dices.sort()
    j = 1
    while True:
        k = bisect.bisect_left(dices, j)
        if k >= len(dices) or len(dices) == 0:
            break
        dices.pop(k)
        j += 1
    print("Case #{}: {}".format(tt + 1, j - 1))
