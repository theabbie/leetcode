class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knw = {}
        for k, v in knowledge:
            knw[k] = v
        openings = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                openings.append(i)
            elif s[i] == ")":
                prev = openings.pop()
                s = s[:prev] + knw.get(s[prev + 1:i], '?') + s[i + 1:]
                i = prev
            i += 1
        return s