from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.store[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_left(self.store[key], (timestamp, "z" * 101))
        if i == 0:
            return ""
        return self.store[key][i - 1][1]