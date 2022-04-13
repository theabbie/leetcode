class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        pos = []
        for i in range(n):
            if boxes[i] == "1":
                pos.append(i)
        return [sum([abs(p - i) for p in pos]) for i in range(n)]