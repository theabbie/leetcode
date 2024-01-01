class Solution:
    def countTestedDevices(self, arr: List[int]) -> int:
        res = 0
        sub = 0
        for el in arr:
            if el - sub > 0:
                res += 1
                sub += 1
        return res