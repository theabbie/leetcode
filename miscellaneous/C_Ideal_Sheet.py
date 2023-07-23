ha, wa = map(int, input().split())

a = []

for _ in range(ha):
    a.append(input())

apos = []

for i in range(ha):
    for j in range(wa):
        if a[i][j] == "#":
            apos.append((i, j))

hb, wb = map(int, input().split())

b = []

for _ in range(hb):
    b.append(input())

bpos = []

for i in range(hb):
    for j in range(wb):
        if b[i][j] == "#":
            bpos.append((i, j))

hc, wc = map(int, input().split())

c = []

for _ in range(hc):
    c.append(input())

cpos = []

for i in range(hc):
    for j in range(wc):
        if c[i][j] == "#":
            cpos.append((i, j))

xx, yy = min(cpos)
cpos = set([(p - xx, q - yy) for p, q in cpos])

def check():
    for x0 in range(-hc, hc + 1):
        for y0 in range(-wc, wc + 1):
            for x1 in range(-hc, hc + 1):
                for y1 in range(-wc, wc + 1):
                    curr = set()
                    for i, j in apos:
                        curr.add((i + x0, j + y0))
                    for i, j in bpos:
                        curr.add((i + x1, j + y1))
                    xx, yy = min(curr)
                    if len(curr) != len(cpos):
                        continue
                    eq = True
                    for x, y in cpos:
                        if (x + xx, y + yy) not in curr:
                            eq = False
                            break
                    if eq:
                        return "Yes"
    return "No"

print(check())