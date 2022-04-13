class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        ctr = {}
        for i in range(n):
            curr = tuple(sorted(dominoes[i]))
            ctr[curr] = ctr.get(curr, 0) + 1
        op = 0
        for pair in ctr:
            op += ctr[pair] * (ctr[pair] - 1) // 2
        return op