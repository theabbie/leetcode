class Solution:
    def format(self, words, a, b, maxWidth, p, isLast):
        n = b - a
        if n == 1 or isLast:
            used = p[b] - p[a] + n - 1
            return " ".join(words[a:b]) + " " * (maxWidth - used)
        spaces = maxWidth - (p[b] - p[a])
        gap = spaces // (n - 1)
        k = spaces % (n - 1)
        res = []
        for i in range(a, b):
            res.append(words[i])
            if i == b - 1:
                break
            if k > 0:
                res.append(" " * (gap + 1))
                k -= 1
            else:
                res.append(" " * gap)
        return "".join(res)
        
    def justify(self, words, maxWidth, p, i, n):
        if i >= n:
            return []
        j = i
        l = 0
        while j < n and l + len(words[j]) <= maxWidth:
            l += len(words[j]) + 1
            j += 1
        rem = self.justify(words, maxWidth, p, j, n)
        return [self.format(words, i, j, maxWidth, p, len(rem) == 0)] + rem
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        p = [0]
        for w in words:
            p.append(p[-1] + len(w))
        return self.justify(words, maxWidth, p, 0, len(words))