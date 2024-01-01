class Bitset:
    def __init__(self, size: int):
        B = int(pow(size, 0.5) + 1)
        blocks = [[set(), set()] for _ in range(B)]
        self.total = 0
        for i in range(size):
            blocks[i // B][0].add(i % B)
        self.B = B
        self.blocks = blocks
        self.size = size

    def fix(self, idx: int) -> None:
        if idx % self.B in self.blocks[idx // self.B][0]:
            self.blocks[idx // self.B][0].remove(idx % self.B)
            self.blocks[idx // self.B][1].add(idx % self.B)
            self.total += 1

    def unfix(self, idx: int) -> None:
        if idx % self.B in self.blocks[idx // self.B][1]:
            self.blocks[idx // self.B][1].remove(idx % self.B)
            self.blocks[idx // self.B][0].add(idx % self.B)
            self.total -= 1

    def flip(self) -> None:
        for idx in range(self.B):
            self.total -= len(self.blocks[idx][1])
            self.blocks[idx].reverse()
            self.total += len(self.blocks[idx][1])

    def all(self) -> bool:
        return self.total == self.size

    def one(self) -> bool:
        return self.total > 0

    def count(self) -> int:
        return self.total

    def toString(self) -> str:
        return "".join("0" if idx % self.B in self.blocks[idx // self.B][0] else "1" for idx in range(self.size))