class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for x, y, r in queries:
            numPoints = 0
            for cx, cy in points:
                if (cx - x) ** 2 + (cy - y) ** 2 <= r ** 2:
                    numPoints += 1
            answer.append(numPoints)
        return answer