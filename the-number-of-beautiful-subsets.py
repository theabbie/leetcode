class Solution:
    def count(self, nums, i, n, used, k, pos):
        if i >= n:
            return 1 if used > 0 else 0
        if used in self.cache:
            return self.cache[used]
        res = self.count(nums, i + 1, n, used, k, pos)
        if pos.get(nums[i] - k, 0) & used == 0:
            res += self.count(nums, i + 1, n, used | (1 << i), k, pos)
        self.cache[used] = res
        return res
    
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        pos = {}
        for i in range(n):
            if nums[i] not in pos:
                pos[nums[i]] = 0
            pos[nums[i]] |= (1 << i)
        used = 0
        self.cache = {}
        return self.count(nums, 0, n, used, k, pos)