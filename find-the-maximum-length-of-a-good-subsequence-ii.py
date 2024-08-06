from collections import *
from sortedcontainers import SortedList

class DICT:
    def __init__(self):
        self.vals = {}
        self.vv = SortedList()
        
    def get(self, key):
        if key in self.vals:
            return self.vals[key]
        return float('-inf')
    
    def set(self, key, val):
        if key in self.vals:
            self.vv.remove(self.vals[key])
        self.vals[key] = val
        self.vv.add(self.vals[key])
        
    def maxwithout(self, key):
        if key in self.vals:
            self.vv.remove(self.vals[key])
        res = float('-inf')
        if len(self.vv) > 0:
            res = self.vv[-1]
        if key in self.vals:
            self.vv.add(self.vals[key])
        return res

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n)]
        mrems = defaultdict(DICT)
        for i in range(n - 1, -1, -1):
            for rem in range(k + 1):
                if rem > 0:
                    dp[i][rem] = max(dp[i][rem], dp[i][rem - 1])
                dp[i][rem] = max(dp[i][rem], 1 + mrems[rem].get(nums[i]))
                if rem == 0:
                    continue
                dp[i][rem] = max(dp[i][rem], 1 + mrems[rem - 1].maxwithout(nums[i]))
            for rem in range(k + 1):
                mrems[rem].set(nums[i], max(mrems[rem].get(nums[i]), dp[i][rem]))
        res = 0
        for i in range(n):
            res = max(res, 1 + dp[i][k])
        return res