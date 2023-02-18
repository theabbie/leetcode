a, b = map(int, input().split())

rows = [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]]

a, b = min(a, b), max(a, b)
apos = bpos = None

for i in range(4):
    if a in rows[i]:
        apos = i
    if b in rows[i]:
        bpos = i

if apos != None and bpos != None and bpos == apos + 1 and rows[bpos].index(b) // 2 == rows[apos].index(a):
    print("Yes")
else:
    print("No")