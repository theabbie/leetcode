import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.cumdist = [0]
        for el in w:
            self.cumdist.append(self.cumdist[-1] + el / total)

    def pickIndex(self) -> int:
        return max(bisect.bisect_left(self.cumdist, random.random()) - 1, 0)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()