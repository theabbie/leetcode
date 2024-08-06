class RangeSum:
    def __init__(self, nums):
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

class Solution:
    def reversePairs(self, arr):
        n = len(arr)
        arr = [(arr[i], i) for i in range(n)]
        arr.sort()
        j = n - 1
        res = 0
        ctr = RangeSum([0] * n)
        for i in range(n - 1, -1, -1):
            while j >= 0 and arr[j][0] > 2 * arr[i][0]:
                ctr.update(arr[j][1], 1)
                j -= 1
            res += ctr.sumRange(0, arr[i][1] - 1)
        return res