from collections import defaultdict

def firstlarger(arr, val):
    beg = 0
    end = len(arr) - 1
    res = float('inf')
    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] > val:
            res = arr[mid]
            end = mid - 1
        else:
            beg = mid + 1
    return res

class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = defaultdict(int)
        for el in nums:
            ctr[el] += 1
        freqs = set()
        for el in ctr:
            freqs.add(ctr[el])
        sf = sorted(freqs)
        res = n
        for s in range(n, 0, -1):
            pos = True
            mul = 0
            while (s + 1) * mul <= n:
                rf = firstlarger(sf, (s + 1) * mul)
                if rf < (s + 1) * (mul + 1) and rf < mul * s + s:
                    pos = False
                    break
                mul += 1
            if pos:
                res = sum(ctr[el] // (s + 1) + int(ctr[el] % (s + 1) > 0) for el in ctr)
                break
        return res