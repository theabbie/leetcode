from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        numpeople = defaultdict(list)
        for i, gsize in enumerate(groupSizes):
            numpeople[gsize].append(i)
        res = []
        for size, people in numpeople.items():
            n = len(people)
            for i in range(0, n, size):
                res.append(people[i:i+size])
        return res