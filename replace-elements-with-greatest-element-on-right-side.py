class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            if i < n - 1:
                arr[i] = max(arr[i + 1 : n])
            else:
                arr[i] = -1
        return arr