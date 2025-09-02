from collections import *
from bisect import *

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        res = [0] * numberOfUsers
        alls = 0
        heres = []
        offlines = defaultdict(list)
        for e in events:
            if e[0] == 'OFFLINE':
                offlines[int(e[2])].append((int(e[1]), int(e[1]) + 60))
            if e[0] == 'MESSAGE':
                if e[2] == 'HERE':
                    heres.append(int(e[1]))
                elif e[2] == 'ALL':
                    alls += 1
                else:
                    for x in map(lambda y: int(y[2:]), e[2].split()):
                        res[x] += 1
        heres.sort()
        for i in range(numberOfUsers):
            res[i] += alls
        for el in range(numberOfUsers):
            arr = sorted(offlines[el])
            prev = float('-inf')
            for x, y in arr:
                res[el] += bisect_right(heres, x - 1) - bisect_left(heres, prev)
                prev = y
            res[el] += bisect_right(heres, float('inf')) - bisect_left(heres, prev)
        return res