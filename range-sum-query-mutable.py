class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = nums
        self.tree = {}
        self.build(0, n, 1)
        
    def build(self, i, j, k):
        if i + 1 == j:
            self.tree[k] = self.nums[i]
            return
        mid = (i + j) // 2
        l = self.build(i, mid, 2 * k)
        r = self.build(mid, j, 2 * k + 1)
        self.tree[k] = self.tree.get(2 * k, 0) + self.tree.get(2 * k + 1, 0)
        
    def upd(self, index, val, i, j, k):
        if i + 1 == j:
            self.tree[k] = val
            return
        mid = (i + j) // 2
        if index < mid:
            self.upd(index, val, i, mid, 2 * k)
        else:
            self.upd(index, val, mid, j, 2 * k + 1)
        self.tree[k] = self.tree.get(2 * k, 0) + self.tree.get(2 * k + 1, 0)
        
    def query(self, x, y, i, j, k):
        if y - 1 < i or x >= j:
            return 0
        if i >= x and j <= y:
            return self.tree[k]
        mid = (i + j) // 2
        return self.query(x, y, i, mid, 2 * k) + self.query(x, y, mid, j, 2 * k + 1)

    def update(self, index: int, val: int) -> None:
        self.upd(index, val, 0, len(self.nums), 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(left, right + 1, 0, len(self.nums), 1)