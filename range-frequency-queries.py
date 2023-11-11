from collections import Counter

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        n = len(arr)
        B = int(pow(n, 0.5) + 1)
        blocks = [Counter() for _ in range(B)]
        for i in range(n):
            blocks[i // B][arr[i]] += 1
        self.B = B
        self.arr = arr
        self.blocks = blocks

    def query(self, left: int, right: int, value: int) -> int:
        i = left
        res = 0
        while i <= right:
            if i % self.B == 0 and i + self.B - 1 <= right:
                res += self.blocks[i // self.B][value]
                i += self.B
            else:
                if self.arr[i] == value:
                    res += 1
                i += 1
        return res