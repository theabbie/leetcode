class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        vals = [(reward1[i] - reward2[i], reward1[i], reward2[i]) for i in range(n)]
        vals.sort(reverse = True)
        res = 0
        for i in range(k):
            res += vals[i][1]
        for i in range(k, n):
            res += vals[i][2]
        return res