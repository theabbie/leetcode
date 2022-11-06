class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        if k == 1:
            ss = s + s
            return min(ss[i:i+n] for i in range(n))
        return "".join(sorted(s))