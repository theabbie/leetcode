tt = int(input())

def minSteps(t, ss, ctr, path, cache, gres, poses):
    if min(ctr) >= 1:
        if len(path) < gres[1]:
            gres[0] = path[:]
            gres[1] = len(path)
        return 0
    key = tuple(ctr)
    if key in cache:
        return cache[key]
    minsteps = float('inf')
    for spos, s in enumerate(ss):
        for i in poses[spos]:
            valid = False
            for j in range(i, i + len(s)):
                if ctr[j] == 0:
                    valid = True
                ctr[j] += 1
            if valid:
                path.append((spos + 1, i + 1))
                minsteps = min(minsteps, 1 + minSteps(t, ss, ctr, path, cache, gres, poses))
                path.pop()
            for j in range(i, i + len(s)):
                ctr[j] -= 1
    cache[key] = minsteps
    return minsteps

for _ in range(tt):
    t = input()
    n = len(t)
    ss = []
    k = int(input())
    for __ in range(k):
        ss.append(input())
    poses = [[] for __ in range(k)]
    for ii in range(k):
        i = t.find(ss[ii], 0)
        while i != -1:
            poses[ii].append(i)
            i = t.find(ss[ii], i + 1)
    gres = [[], float('inf')]
    res = minSteps(t, ss, [0] * n, [], {}, gres, poses)
    if res == float('inf'):
        print(-1)
    else:
        print(res)
        for a, b in gres[0]:
            print(*[a, b])