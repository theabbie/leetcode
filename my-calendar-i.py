import bisect

class MyCalendar:

    def __init__(self):
        self.startinv = []
        self.endinv = []

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_right(self.startinv, (end, start))
        j = bisect.bisect_right(self.endinv, (start, end))
        if i > j:
            return False
        bisect.insort(self.startinv, (start, end))
        bisect.insort(self.endinv, (end, start))
        return True
