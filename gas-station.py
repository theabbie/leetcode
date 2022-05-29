class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0
        abstotal = 0
        res = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            total += diff
            abstotal += diff
            if total < 0:
                total = 0
                res = i + 1
        if abstotal < 0:
            return -1
        return res