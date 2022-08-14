from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        wl = len(words[0])
        wordctr = defaultdict(int)
        l = 0
        for i in range(k):
            wordctr[words[i]] += 1
            l += len(words[i])
        res = []
        for i in range(n - l + 1):
            wcopy = wordctr.copy()
            ctr = k
            j= i
            while j < i + l:
                curr = s[j:j+wl]
                if curr not in wcopy or wcopy[curr] == 0:
                    break
                else:
                    wcopy[curr] -= 1
                    ctr -= 1
                j += wl
            if ctr == 0:
                res.append(i)
        return res