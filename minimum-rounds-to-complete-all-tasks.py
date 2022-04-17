from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        ctr = Counter(tasks)
        for f in ctr.values():
            found = False
            for i in range(f // 3, -1, -1):
                if (f - 3 * i) % 2 == 0:
                    rounds += i + (f - 3 * i) // 2
                    found = True
                    break
            if not found:
                return -1
        return rounds