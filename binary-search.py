class Solution:
    def search(self, nums, target):
        n = len(nums)
        res = -1
        for p in range(20, -1, -1):
            pw = 1 << p
            if res + pw < n and nums[res + pw] < target:
                res += pw
        res += 1
        if res >= n or nums[res] != target:
            return -1
        return res