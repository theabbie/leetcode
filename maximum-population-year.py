import bisect

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pops = []
        for b, d in logs:
            bisect.insort(pops, (b, 1))
            bisect.insort(pops, (d, -1))
        mpop = 0
        mpopyear = None
        curr = 0
        for year, p in pops:
            curr += p
            if curr > mpop:
                mpop = curr
                mpopyear = year
        return mpopyear