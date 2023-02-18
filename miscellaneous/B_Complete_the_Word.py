s = input()

n = len(s)

ctr = [0] * 26

space = 0

res = -1

for i in range(n):
    if s[i] == '?':
        space += 1
    else:
        ctr[ord(s[i]) - ord('A')] += 1
    if i >= 26:
        if s[i - 26] == '?':
            space -= 1
        else:
            ctr[ord(s[i - 26]) - ord('A')] -= 1
    if i >= 25:
        if max(ctr) <= 1 and space == ctr.count(0):
            unused = []
            for j in range(25, -1, -1):
                if ctr[j] == 0:
                    unused.append(chr(ord('A') + j))
            res = list(s)
            for j in range(n):
                if res[j] == '?':
                    if j < i - 25:
                        res[j] = 'A'
                    if i - 25 <= j < i + 1:
                        res[j] = unused.pop()
                    if j >= i + 1:
                        res[j] = 'A'
            res = "".join(res)
            break

print(res)