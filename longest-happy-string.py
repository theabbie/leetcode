import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        op = ""
        heap = []
        for ctr, c in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if ctr > 0:
                heapq.heappush(heap, (-ctr, c))
        while len(heap) > 0:
            currn, currc = heapq.heappop(heap)
            if len(op) < 2 or op[-2:] not in {'aa', 'bb', 'cc'} or op[-1] != currc:
                op += currc
                if currn + 1 < 0:
                    heapq.heappush(heap, (currn + 1, currc))
            else:
                if len(heap) == 0:
                    break
                nextn, nextc = heapq.heappop(heap)
                op += nextc
                heapq.heappush(heap, (currn, currc))
                if nextn + 1 < 0:
                    heapq.heappush(heap, (nextn + 1, nextc))
        return op