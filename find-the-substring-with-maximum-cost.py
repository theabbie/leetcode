class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        val = {}
        for i in range(len(chars)):
            val[chars[i]] = vals[i]
        for i in range(26):
            c = chr(ord('a') + i)
            if c not in val:
                val[c] = i + 1
        res = 0
        maxend = float('-inf')
        for c in s:
            maxend = max(val[c], val[c] + maxend)
            res = max(res, maxend)
        return res