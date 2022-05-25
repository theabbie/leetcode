class BIT:
    def __init__(self, arr):
        self.n = len(arr)
        self.bit = [0] * (self.n + 1)
        for i in range(self.n):
            self.update(i, arr[i])

    def update(self, x, val):
        n = self.n
        i = x + 1
        while i <= n:
            self.bit[i] += val
            i += i & (-i)

    def getSum(self, x):
        i = x + 1
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total


arr = [1,3,5]
n = len(arr)

bit = BIT(arr)

for i in range(n):
    print(bit.getSum(i))
