class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        vals = [[difficulty[i], profit[i]] for i in range(n)]
        vals.sort()
        for i in range(1, n):
            vals[i][1] = max(vals[i][1], vals[i - 1][1])
        res = 0
        for w in worker:
            beg = 0
            end = n - 1
            curr = 0
            while beg <= end:
                mid = (beg + end) // 2
                if vals[mid][0] <= w:
                    curr = vals[mid][1]
                    beg = mid + 1
                else:
                    end = mid - 1
            res += curr
        return res