import bisect

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        count = lambda x: bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)
        for i in [0, n // 4, n // 2, 3 * n // 4, n]:
            for j in [i - 1, i, i + 1]:
                if 0 <= j < n and 4 * count(arr[j]) > n:
                    return arr[j]