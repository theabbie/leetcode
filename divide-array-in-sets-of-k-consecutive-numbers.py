from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        ctr = Counter(nums)
        vals = sorted(ctr.keys())
        for el in vals:
            if ctr[el] == 0:
                continue
            p = ctr[el]
            for x in range(el, el + k):
                if ctr[x] < p:
                    return False
                ctr[x] -= p
        return True