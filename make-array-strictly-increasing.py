class Solution:
    def minops(self, arr, i, n, prev, mp):
        if i >= n:
            return 0
        key = (i, prev)
        if key in self.cache:
            return self.cache[key]
        res = float('inf')
        if arr[i] > prev:
            res = min(res, self.minops(arr, i + 1, n, arr[i], mp))
        if prev in mp:
            res = min(res, 1 + self.minops(arr, i + 1, n, mp[prev], mp))
        self.cache[key] = res
        return res
    
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        m = len(arr1)
        n = len(arr2)
        arr2.sort()
        mp = {}
        i = 0
        for el in sorted(arr1 + arr2 + [-1]):
            while i < n and arr2[i] <= el:
                i += 1
            if i < n:
                mp[el] = arr2[i]
        self.cache = {}
        res = self.minops(arr1, 0, m, -1, mp)
        if res == float('inf'):
            return -1
        return res