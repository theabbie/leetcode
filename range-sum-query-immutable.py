class NumArray:
    def __init__(self, nums: List[int]):
        self.cache = {}
        for i in range(len(nums)):
            self.cache[(i, i + 1)] = nums[i]
        
    def sum(self, l, r):
        if (l, r) in self.cache:
            return self.cache[(l, r)]
        mid = (l + r) // 2
        res = self.sum(l, mid) + self.sum(mid, r)
        self.cache[(l, r)] = res
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self.sum(left, right + 1)