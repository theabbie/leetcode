class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        pos = []
        for i in range(n):
            if number[i] == digit:
                pos.append(i)
        maxVal = float('-inf')
        for j in pos:
            currVal = int("".join([number[i] for i in range(n) if i != j]))
            maxVal = max(maxVal, currVal)
        return str(maxVal)