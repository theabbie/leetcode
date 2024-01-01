class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        B = int(pow(n, 0.5) + 1)
        blocks = [0 for _ in range(B)]
        for i in range(n):
            blocks[i // B] += nums[i]
        self.nums = nums
        self.B = B
        self.blocks = blocks

    def update(self, index: int, val: int) -> None:
        self.blocks[index // self.B] -= self.nums[index]
        self.nums[index] = val
        self.blocks[index // self.B] += self.nums[index]

    def sumRange(self, left: int, right: int) -> int:
        i = left
        res = 0
        while i <= right:
            if i % self.B == 0 and i + self.B - 1 <= right:
                res += self.blocks[i // self.B]
                i += self.B
            else:
                res += self.nums[i]
                i += 1
        return res