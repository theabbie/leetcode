from collections import defaultdict

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        freq = defaultdict(int)
        keys = set()
        for a, b in intervals:
            freq[a] += 1
            freq[b + 1] -= 1
            keys.add(a)
            keys.add(b + 1)
        keys = sorted(keys)
        m = len(keys)
        for i in range(1, m):
            freq[keys[i]] += freq[keys[i - 1]]
        return max(freq.values())