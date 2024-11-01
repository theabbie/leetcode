class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def find(s):
            res = []
            if s.isdigit():
                res.append(int(s))
                return res
            for i in range(len(s)):
                if not s[i].isdigit():
                    a = find(s[:i])
                    b = find(s[i+1:])
                    for x in a:
                        for y in b:
                            res.append(eval(f"{x}{s[i]}{y}"))
            return res
        return sorted(find(expression))