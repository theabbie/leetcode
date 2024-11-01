class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        m = min(workerTimes)
        beg = 1
        end = m * mountainHeight * (mountainHeight + 1) // 2
        @lru_cache(maxsize = None)
        def tt(v):
            beg = 0
            end = v
            while beg <= end:
                mid = (beg + end) // 2
                if mid * (mid + 1) // 2 <= v:
                    beg = mid + 1
                else:
                    end = mid - 1
            return beg - 1
        while beg <= end:
            mid = (beg + end) // 2
            cut = 0
            for el in workerTimes:
                cut += tt(mid // el)
            if cut >= mountainHeight:
                end = mid - 1
            else:
                beg = mid + 1
        return end + 1