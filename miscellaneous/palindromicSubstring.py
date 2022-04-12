class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ctr = 0
        for mask in range(1 << n):
            sub = ""
            for j in range(n):
                if mask & (1 << j):
                    sub += s[j]
            print(sub)
            if len(sub) > 0 and sub == sub[::-1]:
                ctr += 1
        return ctr

print(Solution().countSubstrings("aaa"))