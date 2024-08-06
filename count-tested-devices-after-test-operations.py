class Solution:
    def countTestedDevices(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            if arr[i] > 0:
                res += 1
                for j in range(i + 1, n):
                    arr[j] = max(arr[j] - 1, 0)
        return res