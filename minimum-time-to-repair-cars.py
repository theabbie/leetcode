class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(x):
            res = 0
            for r in ranks:
                res += int((x // r) ** 0.5)
            return res
        end = 1
        while check(end) < cars:
            end *= 2
        beg = end // 2
        while beg <= end:
            mid = (beg + end) // 2
            if check(mid) >= cars:
                end = mid - 1
            else:
                beg = mid + 1
        return end + 1