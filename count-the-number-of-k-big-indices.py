class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        B = 17
        m = min(nums)
        if m < 0:
            nums = [el - m for el in nums]
        res = [0] * n
        MASK = 0
        p = 1 << B
        for b in range(B, -1, -1):
            ctr = defaultdict(lambda: [0, 0])
            for i in range(n - 1, -1, -1):
                if nums[i] & (1 << b):
                    res[i] += ctr[nums[i] & MASK][0]
                    ctr[nums[i] & MASK][1] += 1
                else:
                    ctr[nums[i] & MASK][0] += 1
            MASK |= p
            p //= 2
        return res
    
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        a = self.countSmaller(nums)
        b = self.countSmaller(nums[::-1])
        res = 0
        for i in range(n):
            if a[i] >= k and b[n - i - 1] >= k:
                res += 1
        return res