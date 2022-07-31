from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        minutes = defaultdict(set)
        for uid, minute in logs:
            minutes[uid].add(minute)
        res = defaultdict(int)
        for uid, minutes in minutes.items():
            res[len(minutes)] += 1
        return [res[i] for i in range(1, k + 1)]