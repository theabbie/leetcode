class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count(z):
            def zeroes(v):
                p = 5
                res = 0
                while p <= v:
                    res += v // p
                    p *= 5
                return res
            end = 1
            while zeroes(end) <= z:
                end *= 2
            beg = end // 2
            while beg <= end:
                mid = (beg + end) // 2
                if zeroes(mid) <= z:
                    beg = mid + 1
                else:
                    end = mid - 1
            return beg - 1
        return count(k) - count(k - 1)