from collections import *

class Solution:
    def clearStars(self, s: str) -> str:
        res = []
        pos = defaultdict(list)
        for c in s:
            if c == '*':
                for cc in "abcdefghijklmnopqrstuvwxyz":
                    if len(pos[cc]) > 0:
                        res[pos[cc].pop()] = -1
                        break
            else:
                res.append(c)
                pos[c].append(len(res) - 1)
        return "".join(c for c in res if c != -1)