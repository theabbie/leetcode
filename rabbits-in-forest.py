class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ctr = Counter(answers)
        res = 0
        for x in ctr:
            res += math.ceil(ctr[x] / (x + 1)) * (x + 1)
        return res