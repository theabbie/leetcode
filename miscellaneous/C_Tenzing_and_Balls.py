from collections import defaultdict
import bisect

class RangeModule:

    def __init__(self):
        self.track = []

    def addRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
			
        self.track[start:end] = subtrack

    def removeRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
			
        self.track[start:end] = subtrack
		
    def queryRange(self, left, right):
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)
		
        return start == end and start % 2 == 1

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = defaultdict(lambda: [-1, -1])
    for i in range(n):
        if pos[arr[i]][0] == -1:
            pos[arr[i]][0] = pos[arr[i]][1] = i
        pos[arr[i]][1] = i
    res = 0
    rg = RangeModule()
    rg.addRange(0, n - 1)
    for el in sorted(pos, key = lambda x: pos[x][0] - pos[x][1]):
        rg.removeRange(pos[el][0], pos[el][1])
    print(rg.queryRange(0, n - 1))