class LUPrefix:
    def __init__(self, n: int):
        self.n = n
        self.vals = set()
        self.i = 0

    def upload(self, video: int) -> None:
        self.vals.add(video)
        while (self.i + 1) in self.vals:
            self.i += 1

    def longest(self) -> int:
        return self.i