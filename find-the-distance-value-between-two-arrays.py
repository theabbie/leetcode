class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ctr = 0
        for i in arr1:
            found = False
            for j in arr2:
                if abs(i - j) <= d:
                    found = True
                    break
            if not found:
                ctr += 1
        return ctr