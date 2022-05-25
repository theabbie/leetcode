import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        sub = []
        for w, h in envelopes:
            i = bisect.bisect_left(sub, h)
            if i == len(sub):
                sub.append(h)
            else:
                sub[i] = h
        return len(sub)