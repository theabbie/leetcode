from sortedcontainers import SortedList

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        def ispeak(i):
            if i == 0 or i == n - 1:
                return False
            return nums[i - 1] < nums[i] > nums[i + 1]
        peaks = SortedList()
        for i in range(1, n - 1):
            if ispeak(i):
                peaks.add(i)
        res = []
        for t, x, y in queries:
            if t == 1:
                if x + 1 > y - 1:
                    res.append(0)
                else:
                    res.append(peaks.bisect_right(y - 1) - peaks.bisect_left(x + 1))
            else:
                for xx in range(x - 1, x + 2):
                    if 0 <= xx < n and ispeak(xx):
                        peaks.remove(xx)
                nums[x] = y
                for xx in range(x - 1, x + 2):
                    if 0 <= xx < n and ispeak(xx):
                        peaks.add(xx)
        return res