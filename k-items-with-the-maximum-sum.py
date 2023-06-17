class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        vals = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
        return sum(vals[:k])