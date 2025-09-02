class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        res = 0
        boxes = set(initialBoxes)
        akeys = set()
        done = set()
        while True:
            oldbox = len(boxes)
            oldkey = len(akeys)
            for b in list(boxes):
                if b in akeys:
                    status[b] = 1
            for i in range(n):
                if i in boxes and status[i] == 1:
                    if i not in done:
                        res += candies[i]
                        done.add(i)
                    for k in keys[i]:
                        akeys.add(k)
                    for b in containedBoxes[i]:
                        boxes.add(b)
            if len(boxes) == oldbox and len(akeys) == oldkey:
                break
        return res