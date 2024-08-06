class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        pref = set()
        for el in arr1:
            s = str(el)
            for i in range(1, len(s) + 1):
                pref.add(s[:i])
        for el in arr2:
            s = str(el)
            for i in range(res, len(s) + 1):
                if s[:i] in pref:
                    res = i
        return res