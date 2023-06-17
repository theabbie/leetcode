class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        pos = {}
        for i in range(n):
            if s[i] not in pos:
                pos[s[i]] = []
            pos[s[i]].append(i)
        res = 0
        for w in words:
            prev = -1
            sub = True
            for c in w:
                if c not in pos:
                    sub = False
                    break
                beg = 0
                end = len(pos[c]) - 1
                curr = -1
                while beg <= end:
                    mid = (beg + end) // 2
                    if pos[c][mid] > prev:
                        curr = pos[c][mid]
                        end = mid - 1
                    else:
                        beg = mid + 1
                if curr == -1:
                    sub = False
                    break
                prev = curr
            if sub:
                res += 1
        return res