class Solution:
    def gen(self, curr, k, rem):
        if rem == 0:
            return self.res.append(curr)
        d = curr % 10
        if d + k < 10:
            self.gen(10 * curr + d + k, k, rem - 1)
        if k > 0 and d - k >= 0:
            self.gen(10 * curr + d - k, k, rem - 1)
    
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.res = []
        for i in range(1, 10):
            self.gen(i, k, n - 1)
        return self.res