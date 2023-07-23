n = int(input())

class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] = max(x[j], x[i])

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], x)
            idx |= idx + 1

    def query(self, end):
        x = float('-inf')
        while end:
            x = max(x, self.bit[end - 1])
            end &= end - 1
        return x

boxes = []

mp = {}

for _ in range(n):
    a, b, c = map(int, input().split())
    mp[a] = mp[b] = mp[c] = 0
    boxes.append(tuple(sorted([a, b, c])))

for i, el in enumerate(sorted(mp)):
    mp[el] = i

boxes = [(mp[b[0]], mp[b[1]], mp[b[2]]) for b in boxes]

boxes.sort()

j = n - 1

fw = FenwickTree([float('-inf')] * (len(mp) + 1))

found = False

for i in range(n - 1, -1, -1):
    while j > i and boxes[j][0] > boxes[i][0]:
        fw.update(len(mp) - boxes[j][1] - 1, boxes[j][2])
        j -= 1
    if fw.query(len(mp) - boxes[i][1] - 1) > boxes[i][2]:
        found = True
        break
    
print("Yes" if found else "No")