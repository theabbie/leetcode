class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        seq = sorted(range(n), key = lambda i: -growTime[i])
        res = 0
        totalplant = 0
        for i in seq:
            totalplant += plantTime[i]
            res = max(res, totalplant + growTime[i])
        return res