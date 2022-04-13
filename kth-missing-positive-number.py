class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = set(arr)
        mx = max(arr) + k + 1
        ctr = 0
        for i in range(1, mx):
            if i not in arr:
                ctr += 1
            if ctr == k:
                return i