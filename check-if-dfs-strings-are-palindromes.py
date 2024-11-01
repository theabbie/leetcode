class Solution:
    # s[i : j + 1] is palindrome if P[i + j + 2] >= j - i + 1
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
    
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[parent[i]].append(i)
        ctr = [0] * n
        pos = [0] * n
        v = []
        def dfs(i):
            ctr[i] += 1
            for j in sorted(graph[i]):
                dfs(j)
                ctr[i] += ctr[j]
            v.append(s[i])
            pos[i] = len(v) - 1
        dfs(0)
        pal = self.manachers("".join(v))
        return [pal[2*pos[i]-ctr[i]+3]>=ctr[i] for i in range(n)]