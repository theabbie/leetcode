t = int(input())

for _ in range(t):
    b = []
    input()
    for _ in range(8):
        b.append(input())
    res = None
    for i in range(8):
        if len(set(b[i])) == 1 and b[i][0] != ".":
            res = "R"
    for i in range(8):
        if len(set([b[j][i] for j in range(8)])) == 1 and b[0][i] != ".":
            res = "B"
    print(res)