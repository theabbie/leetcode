class Solution:
    def check(self, freq, n, k, r, minval):
        adds = [0] * (n + 1)
        for i in range(n):
            if i > 0:
                adds[i] += adds[i - 1]
            curr = freq[i] + adds[i]
            if curr < minval:
                diff = minval - curr
                if k >= diff:
                    adds[i] += diff
                    adds[min(i + 2 * r + 1, n)] -= diff
                    k -= diff
                else:
                    return False
        return True
    
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        freq = [0] * (n + 1)
        for i in range(n):
            a = max(i - r, 0)
            b = min(i + r, n - 1)
            freq[a] += stations[i]
            freq[b + 1] -= stations[i]
        for i in range(1, n + 1):
            freq[i] += freq[i - 1]
        freq.pop()
        beg = min(freq)
        end = max(freq) + k
        res = beg
        while beg <= end:
            mid = (beg + end) // 2
            if self.check(freq, n, k, r, mid):
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res