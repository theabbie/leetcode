class Solution:
    def longest(self, arr, i, n, used):
        if i >= n:
            return 0
        key = (i, used)
        if key in self.cache:
            return self.cache[key]
        p = lambda c: ord(c) - ord('a')
        a = float('-inf')
        valid = True
        currused = used
        for c in arr[i]:
            if currused & (1 << p(c)):
                valid = False
                break
            else:
                currused |= 1 << p(c)
        if valid:
            a = len(arr[i]) + self.longest(arr, i + 1, n, currused)
        b = self.longest(arr, i + 1, n, used)
        res = max(a, b)
        self.cache[key] = res
        return res
    
    def maxLength(self, arr: List[str]) -> int:
        self.cache = {}
        return self.longest(arr, 0, len(arr), 0)