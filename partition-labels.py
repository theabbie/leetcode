class Solution:
    def partition(self, s, pos, k, n):
        if k >= n:
            return []
        j = float('-inf')
        for i in range(k, n):
            j = max(pos[s[i]], j)
            if j == i:
                return [i + 1 - k] + self.partition(s, pos, i + 1, n)
    
    def partitionLabels(self, s: str, k = 0) -> List[int]:
        pos = {}
        n = len(s)
        for i, c in enumerate(s):
            pos[c] = i
        return self.partition(s, pos, 0, n)