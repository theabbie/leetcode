class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        mpow = [(0, 1)] * (n + 1)
        pw = [1]
        l = 0
        p = 1
        for i in range(1, n + 1):
            if p * 2 <= i:
                l += 1
                p *= 2
                pw.append(p)
            mpow[i] = (l, p)
        cache = {}
        def get(i, x):
            if x == 0:
                return heights[i]
            k = f"{i,x}"
            if k in cache:
                return cache[k]
            cache[k] = max(get(i, x - 1), get(i + pw[x - 1], x - 1))
            return cache[k]
        def getmax(i, j):
            x, px = mpow[j - i]
            return max(get(i, x), get(j - px, x))
        res = []
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
                if getmax(pos, mid + 1) > val:
                    curr = mid
                    end = mid - 1
                else:
                    beg = mid + 1
            if curr < n:
                res.append(curr)
            else:
                res.append(-1)
        return res