class Solution:
    def guessNumber(self, n: int) -> int:
        beg = 1
        end = n
        if guess(beg) == 0:
            return beg
        if guess(end) == 0:
            return end
        while beg <= end:
            mid = (beg + end) // 2
            curr = guess(mid)
            if curr == 0:
                return mid
            elif curr == -1:
                end = mid
            else:
                beg = mid