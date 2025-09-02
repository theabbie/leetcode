from sortedcontainers import SortedList

class Solution:
    def incremovableSubarrayCount(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        suff = [False] * n
        pref = [False] * n
        pref[0] = suff[n - 1] = True
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1] and suff[i + 1]:
                suff[i] = True
        for i in range(1, n):
            if arr[i] > arr[i - 1] and pref[i - 1]:
                pref[i] = True
        bst = SortedList()
        for j in range(n):
            if j == 0 or pref[j - 1]:
                bst.add(arr[j - 1] if j > 0 else float('-inf'))
            if j == n - 1 or suff[j + 1]:
                res += bst.bisect_right(arr[j + 1] - 1 if j + 1 < n else float('inf'))
        return res