t = int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    times = list(map(int, input().split()))
    # val = sum([(1 + times[i]) * x[i] for i in range(n)]) / (n + sum(times))
    gettime = lambda p: sum([times[i] + abs(p - x[i]) for i in range(n)])
    beg = 0
    end = 10 ** 8
    res = beg
    while beg + 0.01 <= end:
        mid = (beg + end) // 2
        res = mid
        if gettime(mid) < gettime(mid + 0.5) < gettime(mid + 1):
            end = mid - 1
        elif gettime(mid) > gettime(mid - 0.5) > gettime(mid - 1):
            beg = mid + 1
        else:
            break
    print(res)
    #print(min([res - 1, res - 0.5, res, res + 0.5, res + 1], key = gettime))