class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        if n == 0:
            return []
        chars = set(s)
        pos = {}
        for i, c in enumerate(s):
            pos[c] = i
        i = 0
        while i < n:
            j = max(pos[c] for c in s[:i+1])
            if j == i:
                break
            i += 1
        return [i + 1] + self.partitionLabels(s[i+1:])