class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n):
            j = i
            while j < n and arr[j] == arr[i + (j - i) % m]:
                j += 1
            if j >= i + m * k:
                return True
        return False