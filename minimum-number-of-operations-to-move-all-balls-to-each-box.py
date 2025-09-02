class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        poses = [i for i in range(n) if boxes[i] == '1']
        ls, lctr = 0, 0
        rs, rctr = sum(poses), len(poses)
        res = [0] * n
        for i in range(n):
            res[i] = i * lctr - ls + rs - i * rctr
            if boxes[i] == '1':
                ls += i
                lctr += 1
                rs -= i
                rctr -= 1
        return res