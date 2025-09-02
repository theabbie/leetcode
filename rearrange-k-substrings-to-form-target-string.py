class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        def split(x):
            res = []
            for i in range(0, len(x), len(x) // k):
                res.append(x[i:i+len(x)//k])
            return res
        return sorted(split(s)) == sorted(split(t))