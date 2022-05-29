class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        res = []
        if finalSum & 1:
            return res
        i = 1
        while i * (i + 1) <= finalSum:
            res.append(2 * i)
            i += 1
        if i * (i + 1) > finalSum:
            res.pop()
            res.append(finalSum - (i - 1) * (i - 2))
        return res