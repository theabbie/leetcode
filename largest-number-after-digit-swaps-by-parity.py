class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        n = len(num)
        odds = []
        evens = []
        for i in range(n):
            if int(num[i]) & 1:
                odds.append(num[i])
            else:
                evens.append(num[i])
        odds.sort(key = int)
        evens.sort(key = int)
        op = []
        for i in range(n):
            if int(num[i]) & 1:
                op.append(odds.pop())
            else:
                op.append(evens.pop())
        return int("".join(op))