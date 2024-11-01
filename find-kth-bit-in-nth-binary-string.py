class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        inv = lambda x: str(1 - int(x))
        def find(k, n):
            if n == 1:
                return "0"
            x = 1
            for _ in range(n - 2):
                x = 2 * x + 1
            if k == x + 1:
                return "1"
            if k > x + 1:
                return inv(find(2 * x + 2 - k, n - 1))
            return find(k, n - 1)
        return find(k, n)