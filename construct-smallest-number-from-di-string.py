class Solution:
    def find(self, pattern, i, n, res, prev, used):
        if i >= n:
            return True
        if i == 0:
            for curr in range(1, 10):
                res[i] = str(curr)
                if self.find(pattern, i + 1, n, res, str(curr), used | (1 << curr)):
                    return True
                res[i] = ""
        else:
            if pattern[i - 1] == "I":
                for curr in range(int(prev) + 1, 10):
                    res[i] = str(curr)
                    if not used & (1 << curr) and self.find(pattern, i + 1, n, res, str(curr), used | (1 << curr)):
                        return True
                    res[i] = ""
            if pattern[i - 1] == "D":
                for curr in range(1, int(prev)):
                    res[i] = str(curr)
                    if not used & (1 << curr) and self.find(pattern, i + 1, n, res, str(curr), used | (1 << curr)):
                        return True
                    res[i] = ""
        return False
    
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = [""] * (n + 1)
        self.find(pattern, 0, n + 1, res, "", 0)
        return "".join(res)