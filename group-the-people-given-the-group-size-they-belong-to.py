class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        numpeople = {}
        for i, gsize in enumerate(groupSizes):
            numpeople[gsize] = numpeople.get(gsize, []) + [i]
        op = []
        for size in numpeople:
            n = len(numpeople[size])
            if n == size:
                op.append(numpeople[size])
            else:
                for i in range(0, n, size):
                    op.append(numpeople[size][i:i+size])
        return op