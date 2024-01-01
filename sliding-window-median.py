from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        l = SortedList()
        r = SortedList()
        def balance():
            while len(l) < len(r):
                l.add(r.pop(0))
            while len(l) - len(r) > 1:
                r.add(l.pop(-1))
        def add(val):
            if len(r) > 0 and val >= r[0]:
                r.add(val)
            else:
                l.add(val)
            balance()
        def remove(val):
            if len(r) > 0 and val >= r[0]:
                r.remove(val)
            else:
                l.remove(val)
            balance()
        def getmedian():
            if len(l) > len(r):
                return l[-1]
            return (l[-1] + r[0]) / 2
        res = []
        for i in range(n):
            add(nums[i])
            if i >= k:
                remove(nums[i - k])
            if i >= k - 1:
                res.append(getmedian())
        return res