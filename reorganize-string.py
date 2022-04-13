import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        op = ""
        ctr = {}
        for c in s:
            ctr[c] = ctr.get(c, 0) + 1
        heap = [(-n, c) for c, n in ctr.items()]
        hlen = len(heap)
        heapq.heapify(heap)
        while len(heap) > 0:
            currn, currc = heapq.heappop(heap)
            if currc != op[-1] if len(op) > 0 else True:
                op += currc
                if currn + 1 < 0:
                    heapq.heappush(heap, (currn + 1, currc))
            else:
                if len(heap) == 0:
                    return ""
                nextn, nextc = heapq.heappop(heap)
                op += nextc
                heapq.heappush(heap, (currn, currc))
                if nextn + 1 < 0:
                    heapq.heappush(heap, (nextn + 1, nextc))
        return op