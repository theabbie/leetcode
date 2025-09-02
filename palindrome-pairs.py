class Trie:
    def __init__(self):
        self.c = {}
        self.pos = []

class Solution:
    def manachers(self, s):
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            if R > i:
                P[i] = min(R - i, P[2 * C - i])
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        return P

    def pals(self, s):
        n = len(s)
        P = self.manachers(s)
        return {i for i in range(n + 1) if i + P[i + n + 1] >= n}

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ftrie = Trie()
        ltrie = Trie()
        for i, w in enumerate(words):
            for s, trie in [(w, ftrie), (w[::-1], ltrie)]:
                curr = trie
                for c in s:
                    if c not in curr.c:
                        curr.c[c] = Trie()
                    curr = curr.c[c]
                curr.pos.append(i)
        res = [set() for _ in range(len(words))]
        for i, w in enumerate(words):
            for s, trie, rev in [(w, ltrie, False), (w[::-1], ftrie, True)]:
                lens = self.pals(s)
                l = 0
                curr = trie
                for j in curr.pos:
                    if l not in lens:
                        break
                    if i == j:
                        continue
                    res[i].add(j)
                    res[j].add(i)
                for c in s:
                    if c not in curr.c:
                        break
                    curr = curr.c[c]
                    l += 1
                    if l in lens and not (rev and l == len(s)):
                        for j in curr.pos:
                            if i == j:
                                continue
                            if rev:
                                res[j].add(i)
                            else:
                                res[i].add(j)
        return [[i, j] for i, v in enumerate(res) for j in v]