from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ctr = Counter(nums)
        rem = len(nums)
        res = []
        while rem > 0:
            res.append([])
            for el in list(ctr.keys()):
                res[-1].append(el)
                ctr[el] -= 1
                rem -= 1
                if ctr[el] == 0:
                    del ctr[el]
        return res