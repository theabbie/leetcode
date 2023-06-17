from collections import defaultdict

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        k = n // 2
        left = defaultdict(set)
        right = defaultdict(set)
        for mask in range(1 << k):
            s = 0
            ctr = 0
            for i in range(k):
                if mask & (1 << i):
                    s += nums[i]
                    ctr += 1
            left[ctr].add(s)
        for mask in range(1 << (n - k)):
            s = 0
            ctr = 0
            for i in range(n - k):
                if mask & (1 << i):
                    s += nums[k + i]
                    ctr += 1
            right[ctr].add(s)
        for ll in range(1, n):
            if (total * ll) % n != 0:
                continue
            val = (total * ll) // n
            for l in range(ll + 1):
                for ls in left[l]:
                    if val - ls in right[ll - l]:
                        return True
        return False