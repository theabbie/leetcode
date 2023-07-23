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
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(SQRT(n))