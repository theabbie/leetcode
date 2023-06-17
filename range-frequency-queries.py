import bisect

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.pos = {}
        for i, el in enumerate(arr):
            if el not in self.pos:
                self.pos[el] = []
            self.pos[el].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.pos:
            return 0
        return bisect.bisect_right(self.pos[value], right) - bisect.bisect_left(self.pos[value], left)