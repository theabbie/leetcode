class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        beg = min(stations)
        end = sum(stations) + k
        res = beg
        arr = [0] * n
        while beg <= end:
            mid = (beg + end) // 2
            used = 0
            s = 0
            j = 0
            arr[:] = stations
            for i in range(n):
                while j < n and j - i <= r:
                    s += arr[j]
                    j += 1
                if s < mid:
                    diff = mid - s
                    used += diff
                    s -= arr[j - 1]
                    arr[j - 1] += diff
                    s += arr[j - 1]
                if used > k:
                    break
                if i - r >= 0:
                    s -= arr[i - r]
            if used <= k:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res