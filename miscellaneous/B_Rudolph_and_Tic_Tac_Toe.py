t = int(input())

pres = []

for _ in range(t):
    b = []
    for _ in range(3):
        b.append(input())
    won = "DRAW"
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] and b[i][0] != ".":
            won = b[i][0]
            break
        if b[0][i] == b[1][i] == b[2][i] and b[0][i] != ".":
            won = b[0][i]
            break
    if b[0][0] == b[1][1] == b[2][2] and b[0][0] != ".":
        won = b[0][0]
    if b[0][2] == b[1][1] == b[2][0] and b[0][2] != ".":
        won = b[0][2]
    pres.append(str(won))

print("\n".join(pres))