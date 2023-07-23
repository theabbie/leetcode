class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        beg = min(bloomDay)
        end = max(bloomDay)
        res = -1
        while beg <= end:
            mid = (beg + end) // 2
            curr = 0
            i = 0
            while i < n:
                ctr = 1
                while i < n - 1 and (bloomDay[i] <= mid) == (bloomDay[i + 1] <= mid):
                    i += 1
                    ctr += 1
                if bloomDay[i] <= mid:
                    curr += ctr // k
                i += 1
            if curr >= m:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res