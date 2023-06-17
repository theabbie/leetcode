class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        beg = 1
        end = maxSum
        res = -1
        while beg <= end:
            mid = (beg + end) // 2
            currsum = mid * mid
            left = index - mid + 1
            right = index + mid - 1
            if left < 0:
                x = -left
                currsum -= x * (x + 1) // 2
            else:
                currsum += left
            if right >= n:
                x = right - n + 1
                currsum -= x * (x + 1) // 2
            else:
                currsum += n - right - 1
            if currsum <= maxSum:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res