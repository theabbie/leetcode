class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        minDel = float('inf')
        curr = 0
        for i in range(n + 1):
            minDel = min(minDel, i - 2 * curr)
            if i < n and s[i] == 'a':
                curr += 1
        minDel += curr
        return minDel