from collections import *

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def countPairs(self, nums: List[int], k: int) -> int:
        M = max(nums)
        ctr = Counter(nums)
        groups = defaultdict(lambda: [0, 0])
        for el in nums:
            eq = int((el * el) % k == 0)
            groups[k // gcd(k, el)][eq] += 1
        res = 0
        for div in groups:
            mul = 1
            curr = 0
            while div * mul <= M:
                curr += ctr[div * mul]
                mul += 1
            res += groups[div][0] * curr + groups[div][1] * (curr - 1)
        return res // 2