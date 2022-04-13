import bisect

class SORTracker:

    def __init__(self):
        self.places = []
        self.i = 0

    def add(self, name: str, score: int) -> None:
        bisect.insort(self.places, (-score, name))

    def get(self) -> str:
        self.i += 1
        return self.places[self.i - 1][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()