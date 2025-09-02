from sortedcontainers import SortedList

class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        n = len(arr)
        res = 0
        for i in range(n):
            sl = SortedList()
            ctr = lambda l, r: (sl.bisect_right(r) - sl.bisect_left(l)) if l <= r else 0
            for k in range(i + 1, n):
                if abs(arr[i] - arr[k]) <= c:
                    l1, r1 = arr[i] - a, arr[i] + a
                    l2, r2 = arr[k] - b, arr[k] + b
                    res += ctr(max(l1, l2), min(r1, r2))
                sl.add(arr[k])
        return res