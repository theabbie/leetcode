class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        res = 0
        s = list(s)
        while True:
            changes = []
            for i in range(n - 1):
                if s[i] == "0" and s[i + 1] == "1":
                    changes.append(i)
            if len(changes) > 0:
                for i in changes:
                    s[i] = "1"
                    s[i + 1] = "0"
                res += 1
            else:
                break
        return res