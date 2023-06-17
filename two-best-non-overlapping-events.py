class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        mp = {}
        for a, b, c in events:
            mp[a] = mp[b] = 0
        for i, el in enumerate(sorted(mp)):
            mp[el] = i
        events.sort()
        maxscore = [0] * (len(mp) + 1)
        j = n - 1
        maxyet = 0
        for i in range(len(mp), -1, -1):
            while j >= 0 and mp[events[j][0]] >= i:
                maxyet = max(maxyet, events[j][2])
                j -= 1
            maxscore[i] = maxyet
        res = 0
        for a, b, c in events:
            res = max(res, c + maxscore[mp[b] + 1])
        return res