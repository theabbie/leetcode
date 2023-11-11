class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.sums = [0] * (4 * n + 4)
        for i in range(n):
            self.update(i, nums[i])

    def update(self, index, val, k = 1, i = 0, j = None):
        if j == None:
            j = self.n
        if index < i or index >= j:
            return
        if i + 1 == j and i == index:
            self.sums[k] = val
            return
        mid = (i + j) // 2
        self.update(index, val, 2 * k, i, mid)
        self.update(index, val, 2 * k + 1, mid, j)
        self.sums[k] = self.sums[2 * k] + self.sums[2 * k + 1]

    def sumRange(self, l, r, k = 1, i = 0, j = None):
        if j == None:
            j = self.n
        if j <= l or i > r:
            return 0
        if i >= l and j - 1 <= r:
            return self.sums[k]
        mid = (i + j) // 2
        return self.sumRange(l, r, 2 * k, i, mid) + self.sumRange(l, r, 2 * k + 1, mid, j)