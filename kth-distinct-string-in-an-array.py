class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        i = 0
        seen = {}
        for s in arr:
            seen[s] = seen.get(s, 0) + 1
        for s in arr:
            if seen[s] == 1:
                i += 1
            if i == k:
                return s
        return ""