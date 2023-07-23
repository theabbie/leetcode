t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    z = nz = 0
    nzsums = []
    for el in arr:
        if el == 0:
            z += 1
        else:
            nzsums.append(el)
            nz += 1
    if z <= nz + 1:
        print(0)
    else:
        nzsums.sort()
        res = 0
        for xx in range(2):
            sums = {0}
            i = 0
            j = len(nzsums) - 1
            f = xx == 0
            prev = -1
            while i < j:
                if f:
                    if prev != -1:
                        sums.add(prev + nzsums[i])
                    prev = nzsums[i]
                    i += 1
                else:
                    if prev != -1:
                        sums.add(prev + nzsums[j])
                    prev = nzsums[j]
                    j -= 1
                f = not f
            i = 0
            while i in sums:
                i += 1
            res = max(res, i)
        print(res)