class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if s == '':
            return 0.5
        score = 0
        pos = [0]
        ctr = 0
        for i, c in enumerate(s):
            if c == '(':
                ctr += 1
            else:
                ctr -= 1
            if ctr == 0:
                pos.append(i + 1)
        n = len(pos)
        for i in range(n - 1):
            score += 2 * self.scoreOfParentheses(s[pos[i] + 1 : pos[i + 1] - 1])
        return int(score)