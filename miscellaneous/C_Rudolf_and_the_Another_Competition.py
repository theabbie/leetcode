t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())
    scores = []
    for _ in range(n):
        curr = list(map(int, input().split()))
        curr.sort()
        rem = h
        solved = 0
        penalty = 0
        p = 0
        for el in curr:
            if rem >= el:
                rem -= el
                p += el
                solved += 1
                penalty += p
        scores.append((-solved, penalty))
    rank = 1
    for el in scores:
        if el < scores[0]:
            rank += 1
    print(rank)