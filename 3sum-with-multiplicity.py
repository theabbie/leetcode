from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        M = 10 ** 9 + 7
        n = len(arr)
        res = 0
        ctr = Counter()
        for i in range(n):
            for j in range(i + 1, n):
                res += ctr[target - arr[i] - arr[j]]
                res %= M
            ctr[arr[i]] += 1
        return res