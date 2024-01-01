class SparseTable:
    def __init__(self, arr, func, init):
        self.func = func
        self.init = init
        n = len(arr)
        k = n.bit_length()
        table = [[self.init] * k for _ in range(n)]
        self.mpow = [(0, 1)] * (n + 1)
        l = 0
        p = 1
        for i in range(1, n + 1):
            if p * 2 <= i:
                l += 1
                p *= 2
            self.mpow[i] = (l, p)
        for l in range(k):
            for i in range(n):
                if l == 0:
                    table[i][l] = arr[i]
                else:
                    a = table[i][l - 1]
                    b = self.init
                    if i + (1 << l - 1) < n:
                        b = table[i + (1 << l - 1)][l - 1]
                    table[i][l] = self.func(a, b)
        self.table = table

    def query(self, l, r):
        i, p = self.mpow[r - l + 1]
        return self.func(self.table[l][i], self.table[r - p + 1][i])

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        res = []
        sp = SparseTable(heights, lambda x, y: max(x, y), float('-inf'))
        for a, b in queries:
            a, b = min(a, b), max(a, b)
            if a == b:
                res.append(a)
                continue
            if heights[b] > heights[a]:
                res.append(b)
                continue
            val = max(heights[a], heights[b])
            pos = b
            beg = b + 1
            end = n - 1
            curr = n
            while beg <= end:
                mid = (beg + end) // 2
                if sp.query(pos, mid) > val:
                    curr = mid
                    end = mid - 1
                else:
                    beg = mid + 1
            if curr < n:
                res.append(curr)
            else:
                res.append(-1)
        return res