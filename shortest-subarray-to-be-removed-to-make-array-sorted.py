class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        res = n
        suff = [False] * n
        pref = [False] * n
        pref[0] = suff[n - 1] = True
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1] and suff[i + 1]:
                suff[i] = True
                res = min(res, i)
        for i in range(1, n):
            if arr[i] >= arr[i - 1] and pref[i - 1]:
                pref[i] = True
                res = min(res, n - i - 1)
        i = 0
        for j in range(n):
            if suff[j]:
                while i < j and pref[i] and arr[i] <= arr[j]:
                    i += 1
                res = min(res, j - i)
        return res