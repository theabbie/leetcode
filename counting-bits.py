class Solution:
    def countBits(self, n: int) -> List[int]:
        return ["{:b}".format(i).count("1") for i in range(n + 1)]