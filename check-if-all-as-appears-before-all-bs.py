class Solution:
    def checkString(self, s: str) -> bool:
        a = []
        b = []
        for i, c in enumerate(s):
            if c == 'a':
                a.append(i)
            if c == 'b':
                b.append(i)
        for i in a:
            for j in b:
                if i > j:
                    return False
        return True