from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        ctr = Counter(hand)
        vals = sorted(ctr.keys())
        for el in vals:
            if ctr[el] == 0:
                continue
            p = ctr[el]
            for x in range(el, el + groupSize):
                if ctr[x] < p:
                    return False
                ctr[x] -= p
        return True