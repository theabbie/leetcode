n, q = map(int, input().split())

groups = [-1] * n

leaders = {}

for i in range(1, n + 1):
    leaders[i] = i

for t in range(q):
    x = list(map(int, input().split()))
    if x[0] == 1:
        a, b = sorted(x[1:])
        k = a
        while groups[k - 1] != -1:
            k = groups[k - 1]
        groups[b - 1] = k
        leaders[k] = x[2]
    elif x[0] == 1:
        a = x[1]
        k = a
        while groups[k - 1] != -1:
            k = groups[k - 1]
        leaders[k] = a
    else:
        a = x[1]
        k = a
        while groups[k - 1] != -1:
            k = groups[k - 1]
        print(leaders[k])