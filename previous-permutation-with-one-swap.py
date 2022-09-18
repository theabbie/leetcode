class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 2, -1, -1):
            j = max(range(i + 1, n), key = lambda x: arr[x] if arr[x] < arr[i] else float('-inf'))
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                break
        return arr