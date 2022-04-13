class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        mdepth = 0
        for c in s:
            if c == "(":
                depth += 1
            if c == ")":
                depth -= 1
            mdepth = max(mdepth, depth)
        return mdepth