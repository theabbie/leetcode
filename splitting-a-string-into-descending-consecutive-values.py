class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def gen(i, curr):
            if i >= n:
                return len(curr) >= 2
            v = 0
            for j in range(i, n):
                v = 10 * v + int(s[j])
                if len(curr) == 0 or v == curr[-1] - 1:
                    curr.append(v)
                    if gen(j + 1, curr):
                        return True
                    curr.pop()
                if len(curr) > 0 and v >= curr[-1]:
                    break
            return False
        return gen(0, [])