class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        total = sum(arr)
        curr = 0
        f = -1
        s = -1
        for i in range(n):
            curr += arr[i]
            if f < 0 and curr * 3 == total:
                f = i
            if curr * 3 == 2 * total:
                s = i
            if f >= 0 and s >= 0 and f < s and s < n - 1:
                return True
        return False