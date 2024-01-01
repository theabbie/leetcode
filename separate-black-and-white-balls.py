class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        z = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                z += 1
            else:
                res += z
        return res