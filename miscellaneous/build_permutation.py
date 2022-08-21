t = int(input())

for _ in range(t):
    n = int(input())
    res = []
    for i in range(n):
        j = 4 * n * n
        pos = set()
        while j * j >= 1:
            curr = j * j - i
            if 0 <= curr < n:
                pos.add(curr)
            j -= 1
        res.append(pos)
    print(res)