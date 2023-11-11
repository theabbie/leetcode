from collections import defaultdict
import heapq

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        dist = defaultdict(lambda: float('inf'))
        beg = tuple([0] * len(needs))
        dist[beg] = 0
        heap = [(0, beg)]
        while len(heap) > 0:
            cost, curr = heapq.heappop(heap)
            if list(curr) == needs:
                return cost
            for i in range(len(price)):
                if curr[i] + 1 <= needs[i]:
                    newcurr = list(curr)
                    newcurr[i] += 1
                    newcurr = tuple(newcurr)
                    if dist[newcurr] > cost + price[i]:
                        dist[newcurr] = cost + price[i]
                        heapq.heappush(heap, (dist[newcurr], newcurr))
            for offer in special:
                newcurr = list(curr)
                valid = True
                for i in range(len(curr)):
                    if newcurr[i] + offer[i] > needs[i]:
                        valid = False
                        break
                    newcurr[i] += offer[i]
                newcurr = tuple(newcurr)
                if valid and dist[newcurr] > cost + offer[-1]:
                    dist[newcurr] = cost + offer[-1]
                    heapq.heappush(heap, (dist[newcurr], newcurr))
        return -1