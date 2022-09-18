class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        prev = -1
        for i in range(n):
            j =  n - 1
            while j > i and arr[j] >= arr[i]:
                j -= 1
            if i > prev:
                res += 1
            prev = max(prev, j)
        return res