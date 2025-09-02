import heapq

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = []
        heap = [(2, 1, 1)]
        v = {(1, 1)}
        while heap:
            val, i, j = heapq.heappop(heap)
            if val > bound:
                break
            if not res or val != res[-1]:
                res.append(val)
            for a, b in [(i * x, j), (i, j * y)]:
                if (a, b) not in v:
                    v.add((a, b))
                    heapq.heappush(heap, (a + b, a, b))
        return res