class Solution:
    def minTime(self, skill, mana):
        n = len(skill)
        m = len(mana)
        p = [0] * n
        p[0] = skill[0]
        for i in range(1, n):
            p[i] = p[i - 1] + skill[i]
        t = 0
        for j in range(1, m):
            a = mana[j - 1]
            b = mana[j]
            d = p[0] * a
            for i in range(1, n):
                cand = p[i] * a - p[i - 1] * b
                if cand > d:
                    d = cand
            t += d
        return t + p[-1] * mana[-1]