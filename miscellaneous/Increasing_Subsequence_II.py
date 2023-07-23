M = 10 ** 9 + 7

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

arr = list(map(int, input().split()))

mp = {}

for el in arr:
    mp[el] = 0

for i, el in enumerate(sorted(mp)):
    mp[el] = i

dp = FenwickTree([0] * (len(mp) + 1))

res = 0

for el in arr:
    curr = 1 + dp.query(mp[el])
    curr %= M
    dp.update(mp[el], curr)
    res += curr
    res %= M

print(res)