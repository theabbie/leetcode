t = int(input())

def SQRT(N):
    end = 1
    while end * end < N:
        end *= 2
    beg = end // 2
    res = 1
    while beg <= end:
        mid = (beg + end) // 2
        if mid * mid <= N:
            res = mid
            beg = mid + 1
        else:
            end = mid - 1
    return res

for _ in range(t):
    x = int(input())
    if x <= 1000000:
        if x == 1:
            print(-1)
        else:
            print(x - 1, 1, 1)
    else:
        a = SQRT(x - 1000000)
        b = (x - 1000000) // a
        if x - a * b > 1000000:
            b += 1
        print(a, b, x - a * b)