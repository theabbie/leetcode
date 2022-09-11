class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        mleft = float('-inf')
        res = float('-inf')
        for i in range(n):
            res = max(res, mleft + values[i] - i)
            mleft = max(mleft, values[i] + i)
        return res