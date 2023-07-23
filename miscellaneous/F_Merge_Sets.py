n, m = map(int, input().split())

class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x
    
vals = []

mp = {}

for _ in range(n):
    vals.append(sorted(list(map(int, input().split()))))
    for el in vals[-1]:
        mp[el] = 0

for i, el in enumerate(sorted(mp.keys())):
    mp[el] = i

res = 0

fw = FenwickTree([0] * (len(mp) + 1))

for i in range(n - 1, -1, -1):
    for j in range(m):
        res += (j + 1) * (n - i - 1) + fw.query(mp[vals[i][j]])
    for j in range(m):
        fw.update(mp[vals[i][j]], 1)

print(res)