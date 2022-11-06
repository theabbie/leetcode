t = int(input())

for _ in range(t):
    n = int(input())
    M = 3 * n
    i = 0
    j = M - 1
    steps = []
    while i < j:
        steps.append((i + 1, j + 1))
        i += 3
        j -= 3
    print(len(steps))
    for i, j in steps:
        print(i, j)