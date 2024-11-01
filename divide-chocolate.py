class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        beg = 1
        end = sum(sweetness)
        while beg <= end:
            mid = (beg + end) // 2
            s = 0
            cut = 0
            for el in sweetness:
                s += el
                if s >= mid:
                    s = 0
                    cut += 1
            if cut >= k + 1:
                beg = mid + 1
            else:
                end = mid - 1
        return beg - 1