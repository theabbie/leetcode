class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        res = []
        c = 0
        for el in nums:
            if el == -1:
                c += 1
                if c <= len(seen):
                    res.append(seen[-c])
                else:
                    res.append(-1)
            else:
                seen.append(el)
                c = 0
        return res