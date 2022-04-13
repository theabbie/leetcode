class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        beg = 0
        end = num
        while beg <= end:
            mid = (beg + end) // 2
            if mid * mid == num:
                return True
            elif beg == end:
                break
            elif mid * mid > num:
                end = mid
            else:
                beg = mid + 1
        return False