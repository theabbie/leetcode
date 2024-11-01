class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        x, y = destination
        res = []
        for _ in range(x + y):
            right = math.comb(x + y - 1, x)
            down = math.comb(x + y - 1, y)
            for d, ctr, newx, newy in [("H", right, x, y - 1), ("V", down, x - 1, y)]:
                if k > ctr:
                    k -= ctr
                else:
                    x, y = newx, newy
                    res.append(d)
                    break
        return "".join(res)