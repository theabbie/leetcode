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

n = int(input())

h = list(map(int, input().split()))

a = list(map(int, input().split()))

fw = FenwickTree([0] * (n + 1))

res = 0

for i in range(n):
    curr = a[i] + fw.query(h[i])
    fw.update(h[i], curr)
    res = max(res, curr)

print(res)