from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        res = float('inf')
        val = nums[0]
        lsum = rsum = 0
        l = SortedList()
        r = SortedList()
        k -= 1
        def balance():
            nonlocal lsum, rsum
            while len(l) > k:
                x = l.pop(-1)
                r.add(x)
                lsum -= x
                rsum += x
            while len(l) < k and len(r) > 0:
                x = r.pop(0)
                l.add(x)
                rsum -= x
                lsum += x
        def add(val):
            nonlocal lsum, rsum
            if len(r) > 0 and val >= r[0]:
                r.add(val)
                rsum += val
            else:
                l.add(val)
                lsum += val
            balance()
        def remove(val):
            nonlocal lsum, rsum
            if len(r) > 0 and val >= r[0]:
                r.remove(val)
                rsum -= val
            else:
                l.remove(val)
                lsum -= val
            balance()
        nums.pop(0)
        n -= 1
        p = dist + 1
        for i in range(n):
            add(nums[i])
            if i >= p:
                remove(nums[i - p])
            if i >= p - 1 and len(l) == k:
                res = min(res, lsum)
        return res + val