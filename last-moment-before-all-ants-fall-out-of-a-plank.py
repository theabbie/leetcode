class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0
        for el in left:
            res = max(res, el)
        for el in right:
            res = max(res, n - el)
        return res