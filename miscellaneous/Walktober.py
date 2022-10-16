t = int(input())

for tt in range(1, t + 1):
    m, n, p = map(int, input().split())
    scores = []
    for i in range(m):
        scores.append(list(map(int, input().split())))
    res = 0
    mrows = [0] * n
    for i in range(m):
        for j in range(n):
            mrows[j] = max(mrows[j], scores[i][j])
    for i in range(n):
        res += mrows[i] - scores[p - 1][i]
    print(f"Case #{tt}: {res}")