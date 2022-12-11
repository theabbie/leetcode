n, q = map(int, input().split())

s = input()

ap = [0]
bp = [0]
cp = [0]

for c in s:
    ctr = [0, 0, 0]
    ctr["ABC".index(c)] += 1
    ap.append(ap[-1] + ctr[0])
    bp.append(bp[-1] + ctr[1])
    cp.append(cp[-1] + ctr[2])

for _ in range(q):
    l, r = map(int, input().split())
    actr = ap[r] - ap[l - 1]
    bctr = bp[r] - bp[l - 1]
    cctr = cp[r] - cp[l - 1]
    x = int(actr > 0) + int(bctr > 0) + int(cctr > 0) - 1
    print(x)