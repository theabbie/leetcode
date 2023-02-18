class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] != "0":
            return False
        p = [0, 1]
        getp = lambda i: p[len(p) - i - 1] if i < len(p) else 0
        for i in range(n - 2, 0, -1):
            curr = 0
            if s[i] == '0' and getp(minJump - 1) > getp(maxJump):
                curr = 1
            p.append(p[-1] + curr)
        return getp(minJump - 1) > getp(maxJump)