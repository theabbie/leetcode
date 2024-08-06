class Solution:
    def getperm(self, nums, used, prev):
        if used == self.target:
            return 0
        res = float('inf')
        if self.cache[used][prev] != -1:
            return self.cache[used][prev]
        for i in range(len(nums)):
            if not used & (1 << i):
                curr = (abs(nums[i] - prev) if prev != -1 else 0) + (abs(nums[0] - i) if used | (1 << i) == self.target else 0) + self.getperm(nums, used | (1 << i), i)
                res = min(res, curr)
        self.cache[used][prev] = res
        return res
    
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.target = (1 << n) - 1
        self.cache = [[-1] * (n + 1) for _ in range(self.target + 1)]
        res = [0]
        used = 1
        prev = 0
        for _ in range(n - 1):
            curr = (float('inf'), -1)
            for i in range(n):
                if not used & (1 << i):
                    curr = min(curr, ((abs(nums[i] - prev) if prev != -1 else 0) + (abs(nums[0] - i) if used | (1 << i) == self.target else 0) + self.getperm(nums, used | (1 << i), i), i))
            res.append(curr[1])
            used |= (1 << curr[1])
            prev = curr[1]
        return res