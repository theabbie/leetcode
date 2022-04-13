class Solution:
    def isSorted(self, arr, i, n):
        if i == n - 1:
            return True
        if arr[i] <= arr[i + 1] and self.isSorted(arr, i + 1, n):
            return True
        return False
    
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        k = len(strs)
        ctr = 0
        for i in range(n):
            col = [s[i] for s in strs]
            if not self.isSorted(col, 0, k):
                ctr += 1
        return ctr