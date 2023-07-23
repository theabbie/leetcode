from itertools import permutations

m, n = map(int, input().split())

words = []

for i in range(m):
    words.append(input())

pos = set()

for i in range(m):
    for j in range(i + 1, m):
        diff = 0
        for k in range(n):
            if words[i][k] != words[j][k]:
                diff += 1
        if diff == 1:
            pos.add((i, j))
            pos.add((j, i))

perms = permutations(list(range(m)))

def check(perms, pos):
    for p in perms:
        currpos = True
        for i in range(m - 1):
            if (p[i], p[i + 1]) not in pos:
                currpos = False
                break
        if currpos:
            return True
    return False

print("Yes" if check(perms, pos) else "No")