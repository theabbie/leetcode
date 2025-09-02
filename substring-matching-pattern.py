class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        n = len(s)
        a = p.split("*")[0]
        b = p.split("*")[1]
        if a not in s or b not in s:
            return False
        if a in s and b == "":
            return True
        if a == "" and b in s:
            return True
        first = -1
        last = -1
        for i in range(n):
            if s[i:i+len(a)] == a and first == -1:
                first = i + len(a) - 1
            if s[i:i+len(b)] == b:
                last = i
        return first < last