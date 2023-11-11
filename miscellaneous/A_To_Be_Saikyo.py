n = int(input())

p = list(map(int, input().split()))

k = max(p)

ctr = p.count(k)

if k == p[0]:
    if ctr == 1:
        print(k - p[0])
    else:
        print(k - p[0] + 1)
else:
    print(k - p[0] + 1)