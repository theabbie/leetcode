from collections import Counter

class Solution:
    def maxSum(self, arr: List[int], m: int, k: int) -> int:
        n = len(arr)
        ctr = Counter()
        res = 0
        s = 0
        for i in range(n):
            ctr[arr[i]] += 1
            s += arr[i]
            if i >= k:
                s -= arr[i - k]
                ctr[arr[i - k]] -= 1
                if ctr[arr[i - k]] == 0:
                    del ctr[arr[i - k]]
            if i >= k - 1 and len(ctr) >= m:
                res = max(res, s)
        return res