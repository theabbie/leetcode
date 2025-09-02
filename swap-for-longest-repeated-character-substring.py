class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        c = Counter(text)
        v = []
        res = 0
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and text[i] == text[i + 1]:
                i += 1
                ctr += 1
            res = max(res, ctr + int(ctr < c[text[i]]))
            v.append((text[i], ctr))
            i += 1
        for i in range(len(v) - 2):
            if v[i + 1][1] == 1 and v[i][0] == v[i + 2][0]:
                res = max(res, v[i][1] + v[i + 2][1] + int(c[v[i][0]] > v[i][1] + v[i + 2][1]))
        return res