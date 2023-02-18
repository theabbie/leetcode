class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        if target not in words:
            return -1
        res = float('inf')
        for i in range(n):
            if words[i] == target:
                res = min(res, abs(i - startIndex), n + startIndex - i, n + i - startIndex)
        return res