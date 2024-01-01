class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        i = 0
        for a, b, c, m in variables:
            if pow(pow(a, b, 10), c, m) == target:
                res.append(i)
            i += 1
        return res