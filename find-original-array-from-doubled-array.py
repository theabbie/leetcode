from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        ctr = Counter(changed)
        res = []
        changed.sort()
        for el in changed:
            if el != 0 and ctr[el] > 0 and ctr[2 * el] > 0:
                res.append(el)
                ctr[el] -= 1
                ctr[2 * el] -= 1
        res.extend([0] * (ctr[0] // 2))
        if 2 * len(res) != n:
            return []
        return res