M = 10 ** 9 + 7

class Solution:
    def count(self, nums, i, n, rem, used):
        if rem < 0:
            return 0
        if i >= n:
            if rem > 0:
                return 0
            return self.pw[n - used]
        key = (i, rem, used)
        if key in self.cache:
            return self.cache[key]
        res = self.count(nums, i + 1, n, rem, used)
        res += self.count(nums, i + 1, n, rem - nums[i], used + 1)
        res %= M
        self.cache[key] = res
        return res
    
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.cache = {}
        self.pw = [1] * (n + 1)
        for i in range(1, n + 1):
            self.pw[i] = 2 * self.pw[i - 1]
            self.pw[i] %= M
        return self.count(nums, 0, n, k, 0)