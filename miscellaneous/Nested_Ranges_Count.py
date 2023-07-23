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

n = int(input())

ranges = []

mp = {}

for i in range(n):
    a, b = map(int, input().split())
    mp[a] = 0
    mp[b] = 0
    ranges.append((a, b, i))

for i, el in enumerate(sorted(mp.keys())):
    mp[el] = i

ranges.sort(key = lambda p: (p[0], -p[1]))

contains = [0] * n
contained = [0] * n

fw = FenwickTree([0] * (len(mp) + 1))

for i in range(n):
    contained[ranges[i][2]] += fw.query(len(mp) + 1) - fw.query(mp[ranges[i][1]])
    fw.update(mp[ranges[i][1]], 1)

fw = FenwickTree([0] * (len(mp) + 1))

for i in range(n - 1, -1, -1):
    contains[ranges[i][2]] += fw.query(mp[ranges[i][1]] + 1) - fw.query(mp[ranges[i][0]])
    fw.update(mp[ranges[i][1]], 1)

print(*contains)
print(*contained)