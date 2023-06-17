from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:    
        ctr = [senate.count('R'), senate.count('D')]
        senate = deque(senate)
        l = len(senate)
        while min(ctr) > 0:
            r = d = 0
            extraDire = max(ctr[0] - ctr[1], 0)
            extraRad = max(ctr[1] - ctr[0], 0)
            ctr[0] = ctr[1] = 0
            for _ in range(l):
                c = senate.popleft()
                l -= 1
                if c == 'R':
                    if r == 0:
                        if extraRad == 0:
                            senate.append('R')
                            l += 1
                            ctr[0] += 1
                        else:
                            extraRad -= 1
                        d += 1
                    else:
                        r -= 1
                else:
                    if d == 0:
                        if extraDire == 0:
                            senate.append('D')
                            l += 1
                            ctr[1] += 1
                        else:
                            extraDire -= 1
                        r += 1
                    else:
                        d -= 1
        if ctr[0] > 0:
            return "Radiant"
        return "Dire"