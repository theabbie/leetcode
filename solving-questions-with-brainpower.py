class Solution:
    def mostPointsRec(self, questions, i, j, n):
        if i >= n:
            return 0
        if i in self.cache:
            return self.cache[i]
        a = questions[i][0] + self.mostPointsRec(questions, i + questions[i][1] + 1, i + questions[i][1] + 1, n)
        b = self.mostPointsRec(questions, i + 1, j, n)
        res = max(a, b)
        self.cache[i] = res
        return res
    
    def mostPoints(self, questions: List[List[int]]) -> int:
        self.cache = {}
        n = len(questions)
        return self.mostPointsRec(questions, 0, 0, n)