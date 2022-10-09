t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = list(input())
    chunks = []
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and s[i] == s[i + 1]:
            ctr += 1
            i += 1
        i += 1
        chunks.append([s[i - 1], ctr])
    for _ in range(k):
        m = len(chunks)
        for i in range(m):
            if i < m - 1 and chunks[i + 1][0] == "1":
                chunks[i][1] -= 1
            if i > 0 and chunks[i - 1][0] == "1":
                chunks[i][1] -= 1
    print("".join([val * ctr for val, ctr in chunks]))