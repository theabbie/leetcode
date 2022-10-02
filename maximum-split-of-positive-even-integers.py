class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        pos = 0
        i = 1
        while i * (i + 1) <= finalSum:
            k = finalSum - i * (i + 1)
            if k % 2 == 0 and k > 2 * i:
                pos = i
            i += 1
        return [2 * i for i in range(1, pos + 1)] + [finalSum - pos * (pos + 1)]