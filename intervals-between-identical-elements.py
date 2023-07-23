from collections import defaultdict

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        sums = defaultdict(int)
        count = defaultdict(int)
        for i in range(n):
            res[i] += count[arr[i]] * i - sums[arr[i]]
            sums[arr[i]] += i
            count[arr[i]] += 1
        sums = defaultdict(int)
        count = defaultdict(int)
        for i in range(n - 1, -1, -1):
            res[i] += sums[arr[i]] - count[arr[i]] * i
            sums[arr[i]] += i
            count[arr[i]] += 1
        return res