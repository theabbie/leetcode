class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        good = lambda a, b, c, m: pow(pow(a, b, 10), c, m) == target
        return [i for i, el in enumerate(variables) if good(*el)]