M = 10 ** 9 + 7

class Solution:
    def count(self, nums, i, n, zseen, oseen, tseen):
        if i >= n:
            return int(zseen and oseen and tseen)
        key = (i, zseen, oseen, tseen)
        if key in self.cache:
            return self.cache[key]
        res = self.count(nums, i + 1, n, zseen, oseen, tseen)
        if (nums[i] == 0 and not oseen and not tseen) or (nums[i] == 1 and not tseen and zseen) or (nums[i] == 2 and zseen and oseen):
            res += self.count(nums, i + 1, n, zseen or nums[i] == 0, oseen or nums[i] == 1, tseen or nums[i] == 2)
            res %= M
        self.cache[key] = res
        return res
    
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        self.cache = {}
        return self.count(nums, 0, len(nums), False, False, False)