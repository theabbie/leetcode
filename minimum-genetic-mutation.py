from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        paths = deque([(start, 0)])
        seen = set()
        while len(paths) > 0:
            curr, t = paths.pop()
            if curr == end:
                return t
            n = len(curr)
            for i in range(n):
                for c in range(26):
                    mutation = curr[:i] + chr(ord('A') + c) + curr[i + 1:]
                    if mutation in bank and mutation not in seen:
                        paths.appendleft((mutation, t + 1))
                        seen.add(mutation)
        return -1