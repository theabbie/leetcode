class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        if n == 0:
            return len(fruits)
        N = 1
        while N < n:
            N *= 2
        tree = [0] * (2 * N)
        for i in range(n):
            tree[N + i] = baskets[i]
        for i in range(N - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])
        res = 0
        for fruit in fruits:
            if tree[1] < fruit:
                res += 1
                continue
            pos = 1
            while pos < N:
                if tree[2 * pos] >= fruit:
                    pos = 2 * pos
                else:
                    pos = 2 * pos + 1
            tree[pos] = 0
            pos //= 2
            while pos:
                tree[pos] = max(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2
        return res