from collections import Counter

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ctr = Counter()
        for bill in bills:
            ctr[bill] += 1
            if bill == 10:
                if ctr[5] >= 1:
                    ctr[5] -= 1
                else:
                    return False
            elif bill == 20:
                if ctr[10] >= 1 and ctr[5] >= 1:
                    ctr[10] -= 1
                    ctr[5] -= 1
                elif ctr[5] >= 3:
                    ctr[5] -= 3
                else:
                    return False
        return True