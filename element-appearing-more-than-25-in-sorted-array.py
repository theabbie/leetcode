class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ctr = Counter(arr)
        return min([el for el in ctr if ctr[el] * 4 > len(arr)])