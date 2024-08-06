class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for el in grid:
            arr.extend(el)
        arr.sort()
        n = len(arr)
        res = float('inf')
        lsum = 0
        rsum = sum(arr)
        for i in range(n):
            if arr[i] % x != arr[0] % x:
                return -1
            lsum += arr[i]
            rsum -= arr[i]
            lctr = i + 1
            rctr = n - lctr
            curr = lctr * arr[i] - lsum
            curr += rsum - arr[i] * rctr
            res = min(res, curr // x)
        return res