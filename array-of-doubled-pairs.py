from collections import Counter

class Solution:
    def checkPos(self, arr):
        ctr = Counter()
        for el in arr:
            if ctr[el * 2] > 0:
                ctr[2 * el] -= 1
            else:
                ctr[el] += 1
        return sum(ctr.values()) == 0
    
    def canReorderDoubled(self, arr: List[int]) -> bool:
        n = len(arr)
        pos = []
        neg = []
        for el in arr:
            if el >= 0:
                pos.append(el)
            else:
                neg.append(-el)
        pos.sort(reverse = True)
        neg.sort(reverse = True)
        return self.checkPos(pos) and self.checkPos(neg)