class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        i = 0
        firstGap = None
        lastGap = None
        curr = 0
        while i < n:
            ctr = 1
            while i < n -1 and seats[i] == seats[i + 1]:
                ctr += 1
                i += 1
            i += 1
            if seats[i - 1] == 0:
                if not firstGap:
                    firstGap = ctr
                lastGap = ctr
                curr = max(curr, (ctr + 1) // 2)
        if seats[0] == 0:
            curr = max(curr, firstGap)
        if seats[-1] == 0:
            curr = max(curr, lastGap)
        return curr