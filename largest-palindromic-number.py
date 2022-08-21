class Solution:
    def largestPalindromic(self, num: str) -> str:
        ctr = [0] * 10
        for c in num:
            ctr[int(c)] += 1
        res = []
        maxSingle = ""
        for d in range(9, -1, -1):
            if ctr[d] >= 1:
                res.extend([str(d)] * (ctr[d] // 2))
                if ctr[d] % 2 == 1:
                    if maxSingle == "":
                        maxSingle = str(d)
        pal = "".join(res) + maxSingle + "".join(res[::-1])
        n = len(pal)
        i = 0
        while 2 * i < n and pal[i] == pal[n - i - 1] == "0":
            i += 1
        return pal[i:n-i] or "0"