class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        incend = [0] * n
        decstart = [0] * n
        res = 0
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                incend[i] = incend[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                decstart[i] = decstart[i + 1] + 1
        for i in range(n):
            if incend[i] > 0 and decstart[i] > 0:
                res = max(res, incend[i] + decstart[i] + 1)
        return res