class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        numpeople = {}
        for i, gsize in enumerate(groupSizes):
            numpeople[gsize] = numpeople.get(gsize, []) + [i]
        op = []
        for size, people in numpeople.items():
            n = len(people)
            for i in range(0, n, size):
                op.append(people[i:i+size])
        return op