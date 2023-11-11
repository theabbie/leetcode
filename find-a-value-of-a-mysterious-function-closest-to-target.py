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
    def closestToTarget(self, arr: List[int], target: int) -> int:
        n = len(arr)
        sp = SparseTable(arr, lambda x, y: x & y, (1 << 20) - 1)
        res = float('inf')
        for i in range(n):
            beg = i
            end = n - 1
            while beg <= end:
                mid = (beg + end) // 2
                curr = sp.query(i, mid)
                res = min(res, abs(curr - target))
                if curr < target:
                    end = mid - 1
                else:
                    beg = mid + 1
        return res