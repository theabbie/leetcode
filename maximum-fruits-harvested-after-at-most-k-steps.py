class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        l = []
        r = []
        for pos, val in fruits:
            if pos <= startPos:
                l.append((startPos - pos, val))
            else:
                r.append((pos - startPos, val))
        l.reverse()
        def solve(left, right):
            res = 0
            p = [0] * (len(right) + 1)
            for i in range(len(right)):
                p[i + 1] = p[i] + right[i][1]
            taken = 0
            for i in range(len(left)):
                curr = left[i][0]
                if curr > k:
                    break
                taken += left[i][1]
                extra = 0
                if 2 * curr < k:
                    rem = k - 2 * curr
                    beg = 0
                    end = len(right) - 1
                    while beg <= end:
                        mid = (beg + end) // 2
                        if right[mid][0] <= rem:
                            beg = mid + 1
                        else:
                            end = mid - 1
                    extra = p[beg]
                res = max(res, taken + extra)
            return res
        return max(solve(l, r), solve(r, l))