t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    res = 0
    for i in range(n, -1, -1):
        seq = [n, i]
        while seq[-1] > 0 and seq[-2] - seq[-1] <= seq[-1]:
            seq.append(seq[-2] - seq[-1])
        while len(seq) > 0 and seq[-1] < 0:
            seq.pop()
        if len(seq) >= k:
            res += 1
    print(res)