from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = Counter(arr)
    b = []
    rem = n
    while True:
        mex = 0
        while mex in ctr:
            ctr[mex] -= 1
            rem -= 1
            if ctr[mex] == 0:
                del ctr[mex]
            mex += 1
        if mex == 0:
            b.extend([0] * rem)
            break
        b.append(mex)
    print(len(b))
    print(*b)