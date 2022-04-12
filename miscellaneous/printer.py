t = int(input())

for i in range(t):
    colors = []
    for j in range(3):
        colors.append([int(x) for x in input().split()])
    mins = [min([colors[j][k] for j in range(3)]) for k in range(4)]
    total = sum(mins)
    if total < 1000000:
        print("Case #{}: {}".format(i + 1, "IMPOSSIBLE"))
    else:
        extra = total - 1000000
        share = [int(extra * m / total) for m in mins]
        share[-1] = extra - sum(share[:-1])
        for j in range(4):
            mins[j] -= share[j]
        print("Case #{}: {}".format(i + 1, " ".join([str(m) for m in mins])))
