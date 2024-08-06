class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        res = 0
        rem = sum((1 - grumpy[i]) * customers[i] for i in range(n))
        curr = 0
        for i in range(n):
            curr += customers[i]
            rem -= (1 - grumpy[i]) * customers[i]
            if i >= minutes:
                curr -= customers[i - minutes]
                rem += (1 - grumpy[i - minutes]) * customers[i - minutes]
            if i >= minutes - 1:
                res = max(res, curr + rem)
        return res