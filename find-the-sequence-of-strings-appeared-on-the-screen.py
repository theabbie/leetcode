class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        s = ""
        for c in target:
            for x in range(ord(c) - ord('a') + 1):
                res.append(s + chr(ord('a') + x))
            s += c
        return res