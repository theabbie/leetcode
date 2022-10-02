class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        total = 0
        res = 0
        for i in range(n):
            total += arr[i]
            if i >= k:
                total -= arr[i - k]
            if i >= k - 1:
                if total >= threshold * k:
                    res += 1
        return res