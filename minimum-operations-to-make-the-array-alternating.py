from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = [Counter(), Counter()]
        for i in range(n):
            ctr[i % 2][nums[i]] += 1
        res = 0
        evensecmax, evenmax = (0, 0), (0, 0)
        oddsecmax, oddmax = (0, 0), (0, 0)
        for el in ctr[0]:
            temp, evensecmax, evenmax = sorted([evensecmax, evenmax, (ctr[0][el], el)])
        for el in ctr[1]:
            temp, oddsecmax, oddmax = sorted([oddsecmax, oddmax, (ctr[1][el], el)])
        for a in [evensecmax[1], evenmax[1]]:
            for b in [oddsecmax[1], oddmax[1]]:
                if a != b:
                    res = max(res, ctr[0][a] + ctr[1][b])
        return n - res